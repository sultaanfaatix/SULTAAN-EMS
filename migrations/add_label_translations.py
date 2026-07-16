"""
Migration: Add label_translations table for UI label and language customization
This migration creates the LabelTranslation model to support multi-language UI labels
in the Results module and potentially other modules.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models import LabelTranslation
from sqlalchemy import inspect

def upgrade():
    """Create the label_translations table"""
    # Create the table if it doesn't exist
    inspector = inspect(db.engine)
    if not inspector.has_table('label_translations'):
        LabelTranslation.__table__.create(db.engine)
        print("[OK] Created label_translations table")
    else:
        print("[OK] label_translations table already exists")
    
    # Seed with some initial Results module labels in Somali (only if table is empty)
    existing_count = LabelTranslation.query.count()
    if existing_count == 0:
        initial_labels = [
        # Dashboard labels
        ("dashboard_title", "so", "Results Dashboard", "Dashboard"),
        ("academic_year", "so", "Sannad Dugsiyeed", "Dashboard"),
        ("exam", "so", "Imtixaad", "Dashboard"),
        ("total_students", "so", "Wadarta Ardayda", "Dashboard"),
        ("subjects_configured", "so", "Mawduuc la diyaariyay", "Dashboard"),
        ("results_entered", "so", "Natiijada la gudbiyay", "Dashboard"),
        ("active_classes", "so", "Fasalaha firfircoonka ah", "Dashboard"),
        ("select_level", "so", "Dooro Level", "Dashboard"),
        ("select_class", "so", "Dooro Fasalka", "Dashboard"),
        
        # Result Entry labels
        ("result_entry_title", "so", "Gudbinta Natiijada Fasalka", "Result Entry"),
        ("enter_scores", "so", "Gudib tirooyinka", "Result Entry"),
        ("save_all", "so", "Kaydi Dhammaan", "Result Entry"),
        ("reset", "so", "Dib u bilow", "Result Entry"),
        ("student", "so", "Arday", "Result Entry"),
        ("subject", "so", "Mawduuc", "Result Entry"),
        ("score", "so", "Tirada", "Result Entry"),
        ("max_score_entry", "so", "Tirada ugu badan", "Result Entry"),
        ("grade", "so", "Darajada", "Result Entry"),
        ("override", "so", "Beddel darajada", "Result Entry"),
        ("publish", "so", "Daabac", "Result Entry"),
        
        # Class Roster labels
        ("class_roster_title", "so", "Liiska Fasalka", "Class Roster"),
        ("student_id", "so", "Tirada Ardayga", "Class Roster"),
        ("student_name", "so", "Magaca Ardayga", "Class Roster"),
        ("class", "so", "Fasalka", "Class Roster"),
        ("total", "so", "Wadarta", "Class Roster"),
        ("percentage", "so", "Boqolkiiba", "Class Roster"),
        ("grade_point", "so", "Dhibcaha Darajada", "Class Roster"),
        ("export_excel", "so", "Soo saar Excel", "Class Roster"),
        ("export_pdf", "so", "Soo saar PDF", "Class Roster"),
        ("search_student", "so", "Raadi arday (ID ama magac)", "Class Roster"),
        
        # Analytics labels
        ("analytics_title", "so", "Tirada Natiijada", "Analytics"),
        ("grade_distribution", "so", "Qaybinta Darajada", "Analytics"),
        ("subject_performance", "so", "Wadirta Mawduucyada", "Analytics"),
        ("exam_trend", "so", "Trend-ka Imtixaadka", "Analytics"),
        ("pass_fail_ratio", "so", "Nisbadka Guulaha iyo Failure-ka", "Analytics"),
        ("passed", "so", "Laa guuleystay", "Analytics"),
        ("failed", "so", "Laa guuleystay", "Analytics"),
        ("total_results", "so", "Wadarta Natiijada", "Analytics"),
        ("pass_rate", "so", "Nisbadka Guulaha", "Analytics"),
        ("top_performers", "so", "Kii ugu wanaagsan", "Analytics"),
        ("bottom_performers", "so", "Kii ugu xumaan", "Analytics"),
        
        # Grade Management labels
        ("grade_management_title", "so", "Maamulka Darajada", "Grade Management"),
        ("grade_scale", "so", "Shaxda Darajada", "Grade Management"),
        ("min_score", "so", "Tirada ugu yar", "Grade Management"),
        ("max_score", "so", "Tirada ugu badan", "Grade Management"),
        ("grade_point", "so", "Dhibcaha Darajada", "Grade Management"),
        ("status", "so", "Xaaladda", "Grade Management"),
        ("comment", "so", "Sharaxaad", "Grade Management"),
        ("pass", "so", "Guul", "Grade Management"),
        ("fail", "so", "Failure", "Grade Management"),
        ("active", "so", "Firfircoon", "Grade Management"),
        ("preview", "so", "Fiiri", "Grade Management"),
        ("save_grade_scales", "so", "Kaydi Shaxda Darajada", "Grade Management"),
        ("configure_custom", "so", "Dhig Shaxda Gaarka ah", "Grade Management"),
        
        # Settings labels
        ("settings_title", "so", "Settings-ka Results", "Settings"),
        ("label_customization", "so", "Beddelka Erebyada", "Settings"),
        ("language_customization", "so", "Beddelka Luuqadda", "Settings"),
        ("default_language", "so", "Luuqadda Default-ka ah", "Settings"),
        ("add_language", "so", "Ku dar Luuqad", "Settings"),
        ("label_key", "so", "Erebyada Label-ka", "Settings"),
        ("context", "so", "Meesha ka muuqato", "Settings"),
        ("save_labels", "so", "Kaydi Erebyada", "Settings"),
        
        # Quick Setup labels
        ("manage_subjects", "so", "Maamul Mawduucyada", "Dashboard"),
        ("manage_exams", "so", "Maamul Imtixaadka", "Dashboard"),
        ("academic_structure", "so", "Dhismaha Dugsiyeedka", "Dashboard"),
        ("academic_years", "so", "Sannadaha Dugsiyeedka", "Dashboard"),
        ]
        
        added_count = 0
        for label_key, language_code, text_value, context in initial_labels:
            # Check if this label already exists
            existing = LabelTranslation.query.filter_by(label_key=label_key, language_code=language_code).first()
            if not existing:
                label = LabelTranslation(
                    label_key=label_key,
                    language_code=language_code,
                    text_value=text_value,
                    context=context
                )
                db.session.add(label)
                added_count += 1
        
        db.session.commit()
        print(f"[OK] Added {added_count} new label translations in Somali")
    else:
        print(f"[OK] Table already has {existing_count} labels, skipping seed")

def downgrade():
    """Drop the label_translations table"""
    LabelTranslation.__table__.drop(db.engine)
    print("[OK] Dropped label_translations table")

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        print("Running migration: add_label_translations")
        upgrade()
        print("Migration completed successfully!")
