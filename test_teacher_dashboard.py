from app import create_app, db
from app.models import Teacher, User

app = create_app()

with app.app_context():
    teachers = Teacher.query.all()
    print(f'Teacher count: {len(teachers)}')
    for t in teachers[:5]:
        print(f'Teacher: {t.full_name}, ID: {t.id}, User ID: {t.user_id}')
        if t.user:
            print(f'  User: {t.user.username}')
