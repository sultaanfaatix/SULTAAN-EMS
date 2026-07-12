from datetime import datetime
from tempfile import NamedTemporaryFile

from flask import Blueprint, abort, flash, redirect, render_template, request, send_file, url_for
from flask_login import login_required
from openpyxl import Workbook

from . import db
from .audit import audit
from .cloudinary_service import upload_image
from .models import SchoolClass, Setting, Subject, Teacher, TeacherActivity
from .permissions import enforce_endpoint_permission
from .security import ALLOWED_PHOTOS, allowed_file
from .teacher_services import (
    EMPLOYMENT_TYPES,
    SCHOOL_LEVELS,
    TEACHER_PERMISSIONS,
    create_or_update_teacher_user,
    default_teacher_username,
    generate_teacher_code,
    get_teacher_settings,
    log_teacher_activity,
    parse_teacher_form_dates,
    seed_teacher_settings,
    set_teacher_permissions,
    teacher_activity_summary,
    teacher_dashboard_stats,
    teacher_list_query,
    teacher_performance_data,
    teacher_permission_set,
)

teachers_bp = Blueprint("admin_teachers", __name__)


@teachers_bp.before_request
@login_required
def require_login():
    enforce_endpoint_permission()


@teachers_bp.route("/")
def dashboard():
    stats = teacher_dashboard_stats()
    performance = teacher_performance_data()[:5]
    return render_template(
        "admin/teachers/dashboard.html",
        stats=stats,
        performance=performance,
        school_levels=SCHOOL_LEVELS,
    )


@teachers_bp.route("/list")
def teacher_list():
    filters = {
        "q": request.args.get("q", "").strip(),
        "department": request.args.get("department", "").strip(),
        "school_level": request.args.get("school_level", "").strip(),
        "employment_status": request.args.get("employment_status", "").strip(),
        "subject_id": request.args.get("subject_id", "").strip(),
        "class_id": request.args.get("class_id", "").strip(),
    }
    page = max(request.args.get("page", 1, type=int), 1)
    per_page = 15
    pagination = teacher_list_query(filters).paginate(page=page, per_page=per_page, error_out=False)
    departments = [
        row[0]
        for row in db.session.query(Teacher.department).filter(Teacher.department.isnot(None), Teacher.department != "").distinct().order_by(Teacher.department).all()
    ]
    return render_template(
        "admin/teachers/list.html",
        teachers=pagination.items,
        pagination=pagination,
        filters=filters,
        departments=departments,
        subjects=Subject.query.order_by(Subject.sort_order, Subject.name).all(),
        classes=SchoolClass.query.order_by(SchoolClass.name).all(),
        school_levels=SCHOOL_LEVELS,
    )


@teachers_bp.route("/new", methods=["GET", "POST"])
@teachers_bp.route("/<int:teacher_id>/edit", methods=["GET", "POST"])
def teacher_form(teacher_id=None):
    teacher = db.session.get(Teacher, teacher_id) if teacher_id else Teacher()
    subjects = Subject.query.order_by(Subject.sort_order, Subject.name).all()
    classes = SchoolClass.query.order_by(SchoolClass.name).all()
    settings = get_teacher_settings()

    if request.method == "POST":
        try:
            teacher.teacher_id = request.form["teacher_id"].strip()
            if not teacher.teacher_id:
                raise ValueError("Teacher ID is required and must be entered manually.")
            existing_id = Teacher.query.filter(Teacher.teacher_id == teacher.teacher_id, Teacher.id != teacher.id).first()
            if existing_id:
                raise ValueError("Teacher ID already exists.")

            manual_code = request.form.get("teacher_code", "").strip()
            if manual_code:
                if manual_code != (teacher.teacher_code or ""):
                    teacher.teacher_code = generate_teacher_code(manual_code=manual_code)
            elif not teacher.teacher_code:
                teacher.teacher_code = generate_teacher_code()

            teacher.full_name = request.form["full_name"].strip()
            teacher.gender = request.form.get("gender") or None
            teacher.phone = request.form.get("phone", "").strip()
            teacher.email = request.form.get("email", "").strip()
            teacher.address = request.form.get("address", "").strip()
            teacher.emergency_contact = request.form.get("emergency_contact", "").strip()
            teacher.employment_date = parse_teacher_form_dates(request.form.get("employment_date"))
            teacher.employment_type = request.form.get("employment_type") or "Full Time"
            teacher.qualification = request.form.get("qualification", "").strip()
            teacher.years_experience = int(request.form.get("years_experience") or 0)
            teacher.department = request.form.get("department", "").strip()
            teacher.employment_status = request.form.get("employment_status") or settings.get("teacher_default_status") or "Active"
            teacher.school_level = request.form.get("school_level") or None
            teacher.is_active = teacher.employment_status == "Active"

            photo = request.files.get("photo")
            if photo and photo.filename:
                if not allowed_file(photo.filename, ALLOWED_PHOTOS):
                    raise ValueError("Photo must be JPG, PNG, or WEBP.")
                teacher.photo_path = upload_image(photo, "school/teachers")

            selected_subjects = [int(value) for value in request.form.getlist("subject_ids") if value.isdigit()]
            selected_classes = [int(value) for value in request.form.getlist("class_ids") if value.isdigit()]
            teacher.subjects = Subject.query.filter(Subject.id.in_(selected_subjects)).all() if selected_subjects else []
            teacher.classes = SchoolClass.query.filter(SchoolClass.id.in_(selected_classes)).all() if selected_classes else []

            db.session.add(teacher)
            db.session.flush()

            username = request.form.get("username", "").strip() or default_teacher_username(teacher)
            password = request.form.get("password", "")
            confirm = request.form.get("confirm_password", "")
            create_account = bool(request.form.get("create_account"))
            if create_account or teacher.user_id:
                if password and password != confirm:
                    raise ValueError("Passwords do not match.")
                create_or_update_teacher_user(
                    teacher,
                    username=username,
                    password=password,
                    account_active=bool(request.form.get("account_active", "on") == "on"),
                    force_change=bool(request.form.get("force_password_change")),
                )

            log_teacher_activity(teacher, "Profile Updated", f"Saved teacher {teacher.teacher_id} / {teacher.teacher_code}")
            audit("Teacher Updates", f"Saved teacher {teacher.teacher_id} ({teacher.teacher_code})")
            db.session.commit()
            flash("Teacher saved successfully.", "success")
            return redirect(url_for("admin_teachers.teacher_list"))
        except ValueError as exc:
            db.session.rollback()
            flash(str(exc), "danger")

    return render_template(
        "admin/teachers/form.html",
        teacher=teacher,
        subjects=subjects,
        classes=classes,
        settings=settings,
        school_levels=SCHOOL_LEVELS,
        employment_types=EMPLOYMENT_TYPES,
        default_username=default_teacher_username(teacher) if teacher.teacher_id else "",
    )


@teachers_bp.route("/<int:teacher_id>")
def teacher_view(teacher_id):
    teacher = db.session.get(Teacher, teacher_id) or abort(404)
    performance = teacher_performance_data(teacher)[0]
    activity = teacher_activity_summary(teacher)
    return render_template(
        "admin/teachers/view.html",
        teacher=teacher,
        performance=performance,
        activity=activity,
        permissions=teacher_permission_set(teacher),
    )


@teachers_bp.route("/<int:teacher_id>/delete", methods=["POST"])
def delete_teacher(teacher_id):
    teacher = db.session.get(Teacher, teacher_id) or abort(404)
    code = teacher.teacher_code
    teacher_id_value = teacher.teacher_id
    if teacher.user_id:
        user = teacher.user
        teacher.user_id = None
        db.session.flush()
        db.session.delete(user)
    db.session.delete(teacher)
    audit("Teacher Updates", f"Deleted teacher {teacher_id_value} ({code})")
    db.session.commit()
    flash("Teacher deleted.", "success")
    return redirect(url_for("admin_teachers.teacher_list"))


@teachers_bp.route("/<int:teacher_id>/permissions", methods=["GET", "POST"])
def teacher_permissions(teacher_id):
    teacher = db.session.get(Teacher, teacher_id) or abort(404)
    if request.method == "POST":
        posted = request.form.getlist("permissions")
        set_teacher_permissions(teacher, posted)
        log_teacher_activity(teacher, "Permissions Updated", ", ".join(posted))
        audit("Teacher Permissions", f"Updated permissions for {teacher.teacher_id}")
        db.session.commit()
        flash("Teacher permissions saved.", "success")
        return redirect(url_for("admin_teachers.teacher_permissions", teacher_id=teacher.id))
    return render_template(
        "admin/teachers/permissions.html",
        teacher=teacher,
        permissions=TEACHER_PERMISSIONS,
        active_permissions=teacher_permission_set(teacher),
    )


@teachers_bp.route("/performance")
def performance():
    selected_id = request.args.get("teacher_id", type=int)
    teacher = db.session.get(Teacher, selected_id) if selected_id else None
    payloads = teacher_performance_data(teacher)
    return render_template(
        "admin/teachers/performance.html",
        payloads=payloads,
        teachers=Teacher.query.order_by(Teacher.full_name).all(),
        selected_id=selected_id,
    )


@teachers_bp.route("/activity")
def activity():
    teacher_id = request.args.get("teacher_id", type=int)
    teachers = Teacher.query.order_by(Teacher.full_name).all()
    summaries = []
    if teacher_id:
        teacher = db.session.get(Teacher, teacher_id) or abort(404)
        summaries = [teacher_activity_summary(teacher)]
    else:
        summaries = [teacher_activity_summary(teacher) for teacher in teachers[:30]]
    recent = TeacherActivity.query.order_by(TeacherActivity.created_at.desc()).limit(100).all()
    return render_template(
        "admin/teachers/activity.html",
        summaries=summaries,
        teachers=teachers,
        teacher_id=teacher_id,
        recent=recent,
    )


@teachers_bp.route("/settings", methods=["GET", "POST"])
def teacher_settings():
    if request.method == "POST":
        keys = [
            "teacher_code_auto_generate",
            "teacher_code_format",
            "teacher_default_username_format",
            "teacher_password_min_length",
            "teacher_default_password_policy",
            "teacher_theme",
            "teacher_profile_photo_size",
            "teacher_max_upload_size",
            "teacher_default_status",
            "teacher_card_style",
        ]
        for key in keys:
            if key == "teacher_code_auto_generate":
                value = "on" if request.form.get(key) == "on" else "off"
            else:
                value = request.form.get(key, "").strip()
            setting = db.session.get(Setting, key) or Setting(key=key)
            setting.value = value
            db.session.add(setting)
        audit("Teacher Settings", "Updated teacher department settings")
        db.session.commit()
        flash("Teacher settings saved.", "success")
        return redirect(url_for("admin_teachers.teacher_settings"))
    return render_template("admin/teachers/settings.html", settings=get_teacher_settings())


@teachers_bp.route("/export")
def export_teachers():
    wb = Workbook()
    ws = wb.active
    ws.title = "Teachers"
    ws.append(
        [
            "Teacher ID",
            "Teacher Code",
            "Full Name",
            "Phone",
            "Email",
            "Department",
            "School Level",
            "Subjects",
            "Classes",
            "Employment Status",
            "Account Status",
        ]
    )
    for teacher in Teacher.query.order_by(Teacher.full_name).all():
        ws.append(
            [
                teacher.teacher_id,
                teacher.teacher_code,
                teacher.full_name,
                teacher.phone,
                teacher.email,
                teacher.department,
                teacher.school_level,
                ", ".join(subject.name for subject in teacher.subjects),
                ", ".join(school_class.name for school_class in teacher.classes),
                teacher.employment_status,
                "Active" if teacher.is_active else "Inactive",
            ]
        )
    audit("Teacher Export", "Exported teacher list")
    db.session.commit()
    tmp = NamedTemporaryFile(delete=False, suffix=".xlsx")
    wb.save(tmp.name)
    tmp.close()
    return send_file(tmp.name, as_attachment=True, download_name="teachers.xlsx", mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")


@teachers_bp.route("/print")
def print_teachers():
    filters = {
        "q": request.args.get("q", "").strip(),
        "department": request.args.get("department", "").strip(),
        "school_level": request.args.get("school_level", "").strip(),
        "employment_status": request.args.get("employment_status", "").strip(),
        "subject_id": request.args.get("subject_id", "").strip(),
        "class_id": request.args.get("class_id", "").strip(),
    }
    teachers = teacher_list_query(filters).all()
    return render_template("admin/teachers/print.html", teachers=teachers, generated_at=datetime.now())
