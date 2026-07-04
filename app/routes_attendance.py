from collections import Counter
from datetime import date, datetime
from tempfile import NamedTemporaryFile

from flask import Blueprint, abort, flash, redirect, render_template, request, send_file, url_for
from flask_login import current_user, login_required
from openpyxl import Workbook
from sqlalchemy import and_, or_

from . import db
from .audit import audit
from .models import AcademicYear, AttendanceRecord, Exam, SchoolClass, Student
from .permissions import enforce_endpoint_permission
from .services import get_settings

attendance_bp = Blueprint("admin_attendance", __name__)

ATTENDANCE_STATUSES = ["Present", "Absent", "Late", "Excused", "Medical Leave", "Blocked"]


@attendance_bp.before_request
@login_required
def require_login():
    enforce_endpoint_permission()


@attendance_bp.route("/")
def dashboard():
    filters = attendance_filters()
    records = attendance_query(filters).order_by(AttendanceRecord.attendance_date.desc(), AttendanceRecord.updated_at.desc()).limit(500).all()
    students = student_query(filters).order_by(Student.full_name).all()
    stats = Counter(row.status for row in attendance_query(filters).all())
    return render_template(
        "admin/attendance.html",
        records=records,
        students=students,
        stats={status: stats.get(status, 0) for status in ATTENDANCE_STATUSES},
        statuses=ATTENDANCE_STATUSES,
        filters=filters,
        years=AcademicYear.query.order_by(AcademicYear.name.desc()).all(),
        exams=Exam.query.order_by(Exam.id.desc()).all(),
        classes=SchoolClass.query.order_by(SchoolClass.name).all(),
        levels=[value[0] for value in db.session.query(Student.level).filter(Student.level.isnot(None), Student.level != "").distinct().order_by(Student.level).all()],
        sections=[value[0] for value in db.session.query(Student.section).filter(Student.section.isnot(None), Student.section != "").distinct().order_by(Student.section).all()],
        settings=get_settings(),
    )


@attendance_bp.route("/save", methods=["POST"])
def save():
    record_id = request.form.get("record_id")
    record = db.session.get(AttendanceRecord, int(record_id)) if record_id else AttendanceRecord()
    student = db.session.get(Student, int(request.form["student_id"])) or abort(404)
    record.student = student
    record.academic_year = student.academic_year
    record.school_class = student.school_class
    record.exam_id = int(request.form["exam_id"]) if request.form.get("exam_id") else None
    record.attendance_date = parse_date(request.form.get("attendance_date")) or date.today()
    record.status = clean_status(request.form.get("status"))
    record.note = request.form.get("note", "").strip()
    record.marked_by = current_user
    db.session.add(record)
    audit("Attendance Updates", f"Saved {record.status} for {student.student_code} on {record.attendance_date}")
    db.session.commit()
    flash("Attendance saved.", "success")
    return redirect(url_for("admin_attendance.dashboard"))


@attendance_bp.route("/bulk", methods=["POST"])
def bulk():
    student_ids = [int(value) for value in request.form.getlist("student_ids") if value.isdigit()]
    if request.form.get("scope") == "class" and request.form.get("class_id"):
        student_ids = [s.id for s in Student.query.filter_by(class_id=int(request.form["class_id"])).all()]
    if request.form.get("scope") == "level" and request.form.get("level"):
        student_ids = [s.id for s in Student.query.filter_by(level=request.form["level"].strip()).all()]
    if request.form.get("scope") == "section" and request.form.get("section"):
        student_ids = [s.id for s in Student.query.filter_by(section=request.form["section"].strip()).all()]
    if not student_ids:
        flash("Select students before marking attendance.", "warning")
        return redirect(url_for("admin_attendance.dashboard"))
    status = clean_status(request.form.get("status"))
    attendance_date = parse_date(request.form.get("attendance_date")) or date.today()
    exam_id = int(request.form["exam_id"]) if request.form.get("exam_id") else None
    note = request.form.get("note", "").strip()
    for student in Student.query.filter(Student.id.in_(student_ids)).all():
        existing = AttendanceRecord.query.filter_by(student_id=student.id, exam_id=exam_id, attendance_date=attendance_date).first()
        record = existing or AttendanceRecord(student=student, academic_year=student.academic_year, school_class=student.school_class)
        record.exam_id = exam_id
        record.attendance_date = attendance_date
        record.status = status
        record.note = note
        record.marked_by = current_user
        db.session.add(record)
    audit("Attendance Updates", f"Bulk marked {len(student_ids)} students as {status}")
    db.session.commit()
    flash(f"Marked {len(student_ids)} attendance records.", "success")
    return redirect(url_for("admin_attendance.dashboard"))


@attendance_bp.route("/<int:record_id>/delete", methods=["POST"])
def delete(record_id):
    record = db.session.get(AttendanceRecord, record_id) or abort(404)
    audit("Attendance Updates", f"Deleted attendance record {record.id} for {record.student.student_code}")
    db.session.delete(record)
    db.session.commit()
    flash("Attendance record deleted.", "success")
    return redirect(url_for("admin_attendance.dashboard"))


@attendance_bp.route("/export.xlsx")
def export_excel():
    filters = attendance_filters()
    wb = Workbook()
    ws = wb.active
    ws.title = "Attendance"
    ws.append(["Date", "Student ID", "Student Name", "Class", "Academic Year", "Exam", "Status", "Note", "Marked By"])
    for row in attendance_query(filters).order_by(AttendanceRecord.attendance_date.desc()).all():
        ws.append([
            row.attendance_date.isoformat(),
            row.student.student_code,
            row.student.full_name,
            row.school_class.name,
            row.academic_year.name,
            row.exam.name if row.exam else "",
            row.status,
            row.note or "",
            row.marked_by.username if row.marked_by else "",
        ])
    audit("Attendance Export", "Exported attendance Excel")
    db.session.commit()
    tmp = NamedTemporaryFile(delete=False, suffix=".xlsx")
    wb.save(tmp.name)
    tmp.close()
    return send_file(tmp.name, as_attachment=True, download_name="attendance.xlsx")


@attendance_bp.route("/export.pdf")
def export_pdf():
    filters = attendance_filters()
    rows = attendance_query(filters).order_by(AttendanceRecord.attendance_date.desc()).limit(1000).all()
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

    tmp = NamedTemporaryFile(delete=False, suffix=".pdf")
    doc = SimpleDocTemplate(tmp.name, pagesize=landscape(A4), leftMargin=24, rightMargin=24, topMargin=24, bottomMargin=24)
    styles = getSampleStyleSheet()
    data = [["Date", "Student ID", "Name", "Class", "Level", "Section", "Exam", "Status"]]
    for row in rows:
        data.append([
            row.attendance_date.isoformat(),
            row.student.student_code,
            row.student.full_name,
            row.school_class.name,
            row.student.level or "",
            row.student.section or "",
            row.exam.name if row.exam else "Daily",
            row.status,
        ])
    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#002060")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#cbd5e1")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fbff")]),
    ]))
    settings = get_settings()
    doc.build([Paragraph(f"{settings.get('school_name')} Attendance Report", styles["Title"]), Spacer(1, 12), table])
    audit("Attendance Export", "Exported attendance PDF")
    db.session.commit()
    return send_file(tmp.name, as_attachment=True, download_name="attendance.pdf")


@attendance_bp.route("/print")
def print_sheet():
    filters = attendance_filters()
    students = student_query(filters).order_by(Student.full_name).all()
    return render_template(
        "admin/attendance_print.html",
        students=students,
        filters=filters,
        statuses=ATTENDANCE_STATUSES,
        settings=get_settings(),
        today=date.today(),
    )


def attendance_filters():
    return {
        "q": request.args.get("q", "").strip(),
        "year_id": int_or_none(request.args.get("year_id")),
        "exam_id": int_or_none(request.args.get("exam_id")),
        "class_id": int_or_none(request.args.get("class_id")),
        "student_id": int_or_none(request.args.get("student_id")),
        "level": request.args.get("level", "").strip(),
        "section": request.args.get("section", "").strip(),
        "status": request.args.get("status", "").strip(),
        "date": request.args.get("date", "").strip(),
    }


def attendance_query(filters):
    query = AttendanceRecord.query.join(AttendanceRecord.student)
    if filters["q"]:
        q = f"%{filters['q']}%"
        query = query.filter(or_(Student.student_code.like(q), Student.full_name.like(q), AttendanceRecord.note.like(q)))
    for key, column in [
        ("year_id", AttendanceRecord.academic_year_id),
        ("exam_id", AttendanceRecord.exam_id),
        ("class_id", AttendanceRecord.class_id),
        ("student_id", AttendanceRecord.student_id),
    ]:
        if filters[key]:
            query = query.filter(column == filters[key])
    if filters["status"] in ATTENDANCE_STATUSES:
        query = query.filter(AttendanceRecord.status == filters["status"])
    if filters["level"]:
        query = query.filter(Student.level == filters["level"])
    if filters["section"]:
        query = query.filter(Student.section == filters["section"])
    if parse_date(filters["date"]):
        query = query.filter(AttendanceRecord.attendance_date == parse_date(filters["date"]))
    return query


def student_query(filters):
    query = Student.query
    clauses = []
    if filters["year_id"]:
        clauses.append(Student.academic_year_id == filters["year_id"])
    if filters["class_id"]:
        clauses.append(Student.class_id == filters["class_id"])
    if filters["student_id"]:
        clauses.append(Student.id == filters["student_id"])
    if filters["level"]:
        clauses.append(Student.level == filters["level"])
    if filters["section"]:
        clauses.append(Student.section == filters["section"])
    if filters["q"]:
        q = f"%{filters['q']}%"
        clauses.append(or_(Student.student_code.like(q), Student.full_name.like(q)))
    return query.filter(and_(*clauses)) if clauses else query


def int_or_none(value):
    return int(value) if value and str(value).isdigit() else None


def parse_date(value):
    try:
        return datetime.strptime(value, "%Y-%m-%d").date() if value else None
    except ValueError:
        return None


def clean_status(value):
    return value if value in ATTENDANCE_STATUSES else "Present"
