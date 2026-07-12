from app import create_app, db
from app.models import Teacher, User, AcademicLevel, AcademicClass, AcademicSection, Subject

app = create_app()

with app.app_context():
    # Check if test teacher already exists
    existing_teacher = Teacher.query.filter_by(teacher_id='T001').first()
    if existing_teacher:
        print("Test teacher already exists:")
        print(f"  Username: {existing_teacher.user.username if existing_teacher.user else 'N/A'}")
        print(f"  Password: password123")
        print(f"  Full Name: {existing_teacher.full_name}")
    else:
        # Get or create academic structure
        level = AcademicLevel.query.filter_by(name="Form 4").first()
        if not level:
            level = AcademicLevel(name="Form 4", sort_order=4)
            db.session.add(level)
            db.session.flush()
        
        cls = AcademicClass.query.filter_by(name="Form 4A", academic_level_id=level.id).first()
        if not cls:
            cls = AcademicClass(name="Form 4A", academic_level_id=level.id, sort_order=1)
            db.session.add(cls)
            db.session.flush()
        
        section = AcademicSection.query.filter_by(name="Section A", academic_class_id=cls.id).first()
        if not section:
            section = AcademicSection(name="Section A", academic_class_id=cls.id)
            db.session.add(section)
            db.session.flush()
        
        subject = Subject.query.filter_by(name="Mathematics").first()
        if not subject:
            subject = Subject(name="Mathematics")
            db.session.add(subject)
            db.session.flush()
        
        # Create user
        user = User(username='teacher1', full_name='Test Teacher')
        user.set_password('password123')
        db.session.add(user)
        db.session.flush()
        
        # Create teacher
        teacher = Teacher(
            teacher_id='T001',
            teacher_code='TC001',
            full_name='Test Teacher',
            email='teacher@example.com',
            user_id=user.id
        )
        teacher.academic_levels = [level]
        teacher.classes = [cls]
        teacher.sections = [section]
        teacher.subjects = [subject]
        db.session.add(teacher)
        db.session.commit()
        
        print("Test teacher created successfully:")
        print(f"  Username: teacher1")
        print(f"  Password: password123")
        print(f"  Full Name: Test Teacher")
        print(f"  Teacher ID: T001")
        print("\nYou can now login at: http://127.0.0.1:5000/teacher/login")
