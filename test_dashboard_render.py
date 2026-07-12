from app import create_app, db
from app.models import Teacher, User
from app.teacher_analytics import dashboard_summary

app = create_app()

with app.app_context():
    # Create a test teacher if none exists
    teachers = Teacher.query.all()
    if not teachers:
        print("No teachers found. Creating test teacher...")
        from app.models import AcademicLevel, AcademicClass, AcademicSection, Subject
        
        # Create test academic structure
        level = AcademicLevel(name="Form 4", level_order=4)
        db.session.add(level)
        db.session.flush()
        
        cls = AcademicClass(name="Form 4A", academic_level_id=level.id)
        db.session.add(cls)
        db.session.flush()
        
        section = AcademicSection(name="Section A", academic_class_id=cls.id)
        db.session.add(section)
        db.session.flush()
        
        subject = Subject(name="Mathematics", code="MATH")
        db.session.add(subject)
        db.session.flush()
        
        # Create user
        user = User(username='test_teacher')
        user.set_password('password123')
        db.session.add(user)
        db.session.flush()
        
        # Create teacher
        teacher = Teacher(
            teacher_id='T001',
            full_name='Test Teacher',
            email='test@example.com',
            user_id=user.id
        )
        teacher.academic_levels = [level]
        teacher.classes = [cls]
        teacher.sections = [section]
        teacher.subjects = [subject]
        db.session.add(teacher)
        db.session.commit()
        
        print(f"Created test teacher: {teacher.full_name}")
        teachers = [teacher]
    
    # Test dashboard summary
    teacher = teachers[0]
    print(f"\nTesting dashboard summary for: {teacher.full_name}")
    
    try:
        summary = dashboard_summary(teacher, {})
        print("✓ Dashboard summary generated successfully")
        print(f"  Total exams: {summary.get('total_exams', 0)}")
        print(f"  Passed students: {summary.get('passed_students', 0)}")
        print(f"  Failed students: {summary.get('failed_students', 0)}")
        print(f"  Overall average: {summary.get('overall_average', 0)}")
        print(f"  Class performance: {len(summary.get('class_performance', {}).get('top', []))} top classes")
        print(f"  Top students: {len(summary.get('top_students', []))}")
        print(f"  Recent exams: {len(summary.get('recent_exams', []))}")
        print(f"  Grade distribution keys: {list(summary.get('grade_distribution', {}).keys())}")
        print(f"  Important overview keys: {list(summary.get('important_overview', {}).keys())}")
    except Exception as e:
        print(f"✗ Error generating dashboard summary: {e}")
        import traceback
        traceback.print_exc()
