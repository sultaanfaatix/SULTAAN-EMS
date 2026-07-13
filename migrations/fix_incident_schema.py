"""
Fix incident report schema - drop and recreate tables with correct foreign key constraints
This fixes the ON DELETE SET NULL conflict with NOT NULL columns
"""
from app import create_app, db
from app.models import IncidentCategory, SeverityLevel, IncidentAction, IncidentReport, IncidentAttachment


def migrate():
    """Drop and recreate incident tables with correct schema"""
    app = create_app()
    
    with app.app_context():
        print("Dropping existing incident tables...")
        
        # Drop in reverse order of dependencies (SQLite doesn't support CASCADE in DROP TABLE)
        db.session.execute(db.text("DROP TABLE IF EXISTS incident_attachments"))
        db.session.execute(db.text("DROP TABLE IF EXISTS incident_reports"))
        db.session.execute(db.text("DROP TABLE IF EXISTS incident_actions"))
        db.session.execute(db.text("DROP TABLE IF EXISTS severity_levels"))
        db.session.execute(db.text("DROP TABLE IF EXISTS incident_categories"))
        
        db.session.commit()
        
        print("Recreating tables with correct schema...")
        db.create_all()
        
        # Reseed default data
        if not SeverityLevel.query.first():
            severities = [
                {"name": "Minor", "color": "#22c55e", "description": "Minor incident with minimal impact", "sort_order": 1},
                {"name": "Moderate", "color": "#eab308", "description": "Moderate incident requiring attention", "sort_order": 2},
                {"name": "Serious", "color": "#f97316", "description": "Serious incident with significant impact", "sort_order": 3},
                {"name": "Critical", "color": "#ef4444", "description": "Critical incident requiring immediate action", "sort_order": 4},
            ]
            for s in severities:
                db.session.add(SeverityLevel(**s))
        
        if not IncidentCategory.query.first():
            categories = [
                {"name": "Talking During Exam", "description": "Student was talking during examination", "sort_order": 1},
                {"name": "Cheating Attempt", "description": "Attempted to cheat during exam", "sort_order": 2},
                {"name": "Using Mobile Phone", "description": "Used mobile phone during examination", "sort_order": 3},
                {"name": "Possession of Unauthorized Materials", "description": "Had unauthorized materials during exam", "sort_order": 4},
                {"name": "Disturbing Other Students", "description": "Disturbed other students during exam", "sort_order": 5},
                {"name": "Disrespecting Invigilator", "description": "Showed disrespect to exam invigilator", "sort_order": 6},
                {"name": "Late Arrival", "description": "Arrived late to examination", "sort_order": 7},
                {"name": "Seat Switching", "description": "Switched seats without permission", "sort_order": 8},
                {"name": "Impersonation", "description": "Attempted to impersonate another student", "sort_order": 9},
                {"name": "Other", "description": "Other type of incident", "sort_order": 10},
            ]
            for c in categories:
                db.session.add(IncidentCategory(**c))
        
        if not IncidentAction.query.first():
            actions = [
                {"name": "Warning Given", "description": "Verbal or written warning issued", "sort_order": 1},
                {"name": "Seat Changed", "description": "Student moved to different seat", "sort_order": 2},
                {"name": "Answer Sheet Collected", "description": "Answer sheet was collected", "sort_order": 3},
                {"name": "Mobile Phone Confiscated", "description": "Mobile phone was confiscated", "sort_order": 4},
                {"name": "Student Removed From Exam", "description": "Student was removed from examination", "sort_order": 5},
                {"name": "Sent to Administration", "description": "Student sent to administration office", "sort_order": 6},
                {"name": "Exam Cancelled", "description": "Examination was cancelled", "sort_order": 7},
                {"name": "Other", "description": "Other action taken", "sort_order": 8},
            ]
            for a in actions:
                db.session.add(IncidentAction(**a))
        
        db.session.commit()
        print("Schema fix completed successfully")
        print("Tables recreated with ON DELETE RESTRICT for category_id and severity_id")


if __name__ == "__main__":
    migrate()
