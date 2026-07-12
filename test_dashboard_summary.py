from app import create_app, db
from app.models import Teacher, User
from app.teacher_analytics import dashboard_summary

app = create_app()

with app.app_context():
    teachers = Teacher.query.all()
    print(f'Teacher count: {len(teachers)}')
    
    if teachers:
        teacher = teachers[0]
        print(f'Testing with teacher: {teacher.full_name}')
        try:
            summary = dashboard_summary(teacher, {})
            print('Dashboard summary generated successfully')
            print(f'Total exams: {summary.get("total_exams", 0)}')
        except Exception as e:
            print(f'Error generating dashboard summary: {e}')
            import traceback
            traceback.print_exc()
    else:
        print('No teachers found in database')
        print('Creating a test teacher...')
        # Create a test user and teacher
        user = User(username='test_teacher', email='test@example.com')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
        
        teacher = Teacher(
            teacher_id='T001',
            full_name='Test Teacher',
            email='test@example.com',
            user_id=user.id
        )
        db.session.add(teacher)
        db.session.commit()
        
        print(f'Created teacher: {teacher.full_name}')
        
        try:
            summary = dashboard_summary(teacher, {})
            print('Dashboard summary generated successfully')
            print(f'Total exams: {summary.get("total_exams", 0)}')
        except Exception as e:
            print(f'Error generating dashboard summary: {e}')
            import traceback
            traceback.print_exc()
