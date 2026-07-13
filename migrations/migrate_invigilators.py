"""
Migration script for Exam Invigilator System
Creates tables for invigilators, login history, and incident report settings
"""
import sys
sys.path.insert(0, '..')

from datetime import datetime
from app import create_app, db
from app.models import ExamInvigilator, IncidentReportSettings


def migrate():
    """Create invigilator system tables and seed default settings"""
    app = create_app()
    
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Seed default incident report settings
        default_settings = [
            # Field visibility settings
            {"key": "show_student_photo", "value": "true", "type": "boolean", "category": "fields", "description": "Show student photo in incident form"},
            {"key": "show_student_info", "value": "true", "type": "boolean", "category": "fields", "description": "Show student information section"},
            {"key": "show_exam_room", "value": "true", "type": "boolean", "category": "fields", "description": "Show exam room field"},
            {"key": "show_exam", "value": "true", "type": "boolean", "category": "fields", "description": "Show exam selection"},
            {"key": "show_subject", "value": "true", "type": "boolean", "category": "fields", "description": "Show subject selection"},
            {"key": "show_teacher_info", "value": "true", "type": "boolean", "category": "fields", "description": "Show teacher information fields"},
            {"key": "show_evidence_upload", "value": "true", "type": "boolean", "category": "fields", "description": "Show evidence upload section"},
            
            # Field requirement settings
            {"key": "require_exam_room", "value": "false", "type": "boolean", "category": "requirements", "description": "Require exam room field"},
            {"key": "require_exam", "value": "false", "type": "boolean", "category": "requirements", "description": "Require exam selection"},
            {"key": "require_subject", "value": "false", "type": "boolean", "category": "requirements", "description": "Require subject selection"},
            {"key": "require_teacher_name", "value": "false", "type": "boolean", "category": "requirements", "description": "Require teacher name"},
            {"key": "require_teacher_id", "value": "false", "type": "boolean", "category": "requirements", "description": "Require teacher ID"},
            {"key": "require_evidence", "value": "false", "type": "boolean", "category": "requirements", "description": "Require evidence upload"},
            
            # Custom labels
            {"key": "label_exam_room", "value": "Exam Room", "type": "string", "category": "labels", "description": "Label for exam room field"},
            {"key": "label_teacher_name", "value": "Invigilator Name", "type": "string", "category": "labels", "description": "Label for teacher name field"},
            {"key": "label_teacher_id", "value": "Invigilator ID", "type": "string", "category": "labels", "description": "Label for teacher ID field"},
            {"key": "label_description", "value": "Incident Description", "type": "string", "category": "labels", "description": "Label for description field"},
            {"key": "label_actions_taken", "value": "Actions Taken", "type": "string", "category": "labels", "description": "Label for actions taken field"},
            
            # Styling settings
            {"key": "template", "value": "premium", "type": "string", "category": "styling", "description": "Form template (classic, premium, modern, government, university)"},
            {"key": "primary_color", "value": "#3b82f6", "type": "string", "category": "styling", "description": "Primary color"},
            {"key": "secondary_color", "value": "#1e40af", "type": "string", "category": "styling", "description": "Secondary color"},
            {"key": "background_color", "value": "#f8fafc", "type": "string", "category": "styling", "description": "Background color"},
            {"key": "card_background", "value": "#ffffff", "type": "string", "category": "styling", "description": "Card background color"},
            {"key": "font_family", "value": "Segoe UI", "type": "string", "category": "styling", "description": "Font family"},
            {"key": "font_size", "value": "16", "type": "integer", "category": "styling", "description": "Base font size in pixels"},
            
            # Header settings
            {"key": "show_header", "value": "true", "type": "boolean", "category": "header", "description": "Show form header"},
            {"key": "header_title", "value": "Incident Report", "type": "string", "category": "header", "description": "Header title"},
            {"key": "header_subtitle", "value": "Submit examination incident report", "type": "string", "category": "header", "description": "Header subtitle"},
            
            # Footer settings
            {"key": "show_footer", "value": "true", "type": "boolean", "category": "footer", "description": "Show form footer"},
            {"key": "footer_text", "value": "© 2024 Examination System", "type": "string", "category": "footer", "description": "Footer text"},
        ]
        
        for setting in default_settings:
            if not IncidentReportSettings.query.filter_by(setting_key=setting["key"]).first():
                db.session.add(IncidentReportSettings(
                    setting_key=setting["key"],
                    setting_value=setting["value"],
                    setting_type=setting["type"],
                    category=setting["category"],
                    description=setting["description"]
                ))
        
        db.session.commit()
        print("Exam Invigilator System migration completed successfully")
        print("Created tables: exam_invigilators, invigilator_login_history, incident_report_settings")
        print("Seeded default incident report settings")


if __name__ == "__main__":
    migrate()
