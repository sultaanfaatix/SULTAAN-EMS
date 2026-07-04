import secrets
import calendar
from datetime import date
from tempfile import NamedTemporaryFile

from flask import Blueprint, abort, flash, redirect, render_template, request, send_file, url_for
from flask_login import login_required
from sqlalchemy import or_

from . import db
from .audit import audit
from .models import AcademicYear, IdCardIssue, SchoolClass, Setting, Student
from .permissions import enforce_endpoint_permission
from .services import get_settings
from .verification import id_card_qr_payload

id_cards_bp = Blueprint("admin_id_cards", __name__)


@id_cards_bp.before_request
@login_required
def require_login():
    enforce_endpoint_permission()


@id_cards_bp.route("/", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        editable_keys = [
            "id_card_size", "id_card_orientation", "id_card_background", "id_card_primary_color",
            "id_card_accent_color", "id_card_font_family", "id_card_border_style", "id_card_rounded_corners",
            "id_card_show_barcode", "id_card_footer", "id_card_watermark", "id_card_issue_months",
            "id_card_office_signature", "id_card_stamp_text",
        ]
        for key in editable_keys:
            setting = db.session.get(Setting, key) or Setting(key=key)
            setting.value = request.form.get(key, "").strip()
            db.session.add(setting)
        audit("Settings Changes", "Updated ID card designer settings")
        db.session.commit()
        flash("ID card designer saved.", "success")
        return redirect(url_for("admin_id_cards.dashboard"))

    filters = card_filters()
    students = filtered_students(filters).order_by(Student.full_name).limit(500).all()
    issues = IdCardIssue.query.order_by(IdCardIssue.updated_at.desc()).limit(200).all()
    return render_template(
        "admin/id_cards.html",
        settings=get_settings(),
        students=students,
        issues=issues,
        filters=filters,
        classes=SchoolClass.query.order_by(SchoolClass.name).all(),
        years=AcademicYear.query.order_by(AcademicYear.name.desc()).all(),
        levels=distinct_values(Student.level),
        sections=distinct_values(Student.section),
    )


@id_cards_bp.route("/generate/<int:student_id>", methods=["POST"])
def generate(student_id):
    student = db.session.get(Student, student_id) or abort(404)
    issue = get_or_create_issue(student)
    audit("ID Card Operations", f"Generated ID card for {student.student_code}")
    db.session.commit()
    flash("ID card generated.", "success")
    return redirect(url_for("admin_id_cards.print_cards", issue_ids=issue.id))


@id_cards_bp.route("/bulk-generate", methods=["POST"])
def bulk_generate():
    scope = request.form.get("scope", "selected")
    ids = [int(value) for value in request.form.getlist("student_ids") if value.isdigit()]
    query = Student.query
    if scope == "class" and request.form.get("class_id"):
        query = query.filter_by(class_id=int(request.form["class_id"]))
        ids = [s.id for s in query.all()]
    elif scope == "level" and request.form.get("level"):
        ids = [s.id for s in query.filter_by(level=request.form["level"].strip()).all()]
    elif scope == "section" and request.form.get("section"):
        ids = [s.id for s in query.filter_by(section=request.form["section"].strip()).all()]
    elif scope == "all":
        ids = [s.id for s in query.all()]
    if not ids:
        flash("Select students or choose a valid bulk scope.", "warning")
        return redirect(url_for("admin_id_cards.dashboard"))
    issue_ids = []
    for student in Student.query.filter(Student.id.in_(ids)).all():
        issue_ids.append(get_or_create_issue(student).id)
    audit("ID Card Operations", f"Bulk generated {len(issue_ids)} ID cards")
    db.session.commit()
    flash(f"Generated {len(issue_ids)} ID cards.", "success")
    return redirect(url_for("admin_id_cards.print_cards", issue_ids=",".join(str(i) for i in issue_ids)))


@id_cards_bp.route("/print")
def print_cards():
    issues = selected_issues()
    cards = [{"issue": issue, "qr": id_card_qr_payload(issue)} for issue in issues]
    return render_template("admin/id_card_print.html", cards=cards, settings=get_settings())


@id_cards_bp.route("/export.pdf")
def export_pdf():
    issues = selected_issues()
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

    tmp = NamedTemporaryFile(delete=False, suffix=".pdf")
    doc = SimpleDocTemplate(tmp.name, pagesize=A4, leftMargin=24, rightMargin=24, topMargin=24, bottomMargin=24)
    styles = getSampleStyleSheet()
    data = [["Student ID", "Name", "Class", "Year", "Issue Date", "Expiry", "Status"]]
    for issue in issues:
        data.append([
            issue.student.student_code,
            issue.student.full_name,
            issue.student.school_class.name,
            issue.academic_year.name,
            issue.issue_date.isoformat(),
            issue.expiry_date.isoformat() if issue.expiry_date else "",
            issue.status,
        ])
    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#002060")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#cbd5e1")),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
    ]))
    doc.build([Paragraph("Student ID Cards Export", styles["Title"]), Spacer(1, 12), table])
    audit("ID Card Operations", "Exported ID cards PDF")
    db.session.commit()
    return send_file(tmp.name, as_attachment=True, download_name="student_id_cards.pdf")


def get_or_create_issue(student):
    issue = IdCardIssue.query.filter_by(student_id=student.id, academic_year_id=student.academic_year_id, status="Active").first()
    settings = get_settings()
    months = int(settings.get("id_card_issue_months") or 12)
    if not issue:
        issue = IdCardIssue(
            token=secrets.token_urlsafe(32),
            student=student,
            academic_year=student.academic_year,
            issue_date=date.today(),
            expiry_date=add_months(date.today(), months),
            status="Active",
        )
        db.session.add(issue)
        db.session.flush()
    return issue


def selected_issues():
    raw = request.args.get("issue_ids", "")
    ids = [int(value) for value in raw.split(",") if value.isdigit()]
    if ids:
        return IdCardIssue.query.filter(IdCardIssue.id.in_(ids)).order_by(IdCardIssue.id).all()
    return IdCardIssue.query.order_by(IdCardIssue.updated_at.desc()).limit(50).all()


def card_filters():
    return {
        "q": request.args.get("q", "").strip(),
        "class_id": int_or_none(request.args.get("class_id")),
        "year_id": int_or_none(request.args.get("year_id")),
        "level": request.args.get("level", "").strip(),
        "section": request.args.get("section", "").strip(),
    }


def filtered_students(filters):
    query = Student.query
    if filters["q"]:
        q = f"%{filters['q']}%"
        query = query.filter(or_(Student.student_code.like(q), Student.full_name.like(q), Student.mother_name.like(q)))
    if filters["class_id"]:
        query = query.filter(Student.class_id == filters["class_id"])
    if filters["year_id"]:
        query = query.filter(Student.academic_year_id == filters["year_id"])
    if filters["level"]:
        query = query.filter(Student.level == filters["level"])
    if filters["section"]:
        query = query.filter(Student.section == filters["section"])
    return query


def distinct_values(column):
    return [value[0] for value in db.session.query(column).filter(column.isnot(None), column != "").distinct().order_by(column).all()]


def int_or_none(value):
    return int(value) if value and str(value).isdigit() else None


def add_months(value, months):
    month = value.month - 1 + months
    year = value.year + month // 12
    month = month % 12 + 1
    day = min(value.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)
