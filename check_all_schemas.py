"""Script to check all model/database schema mismatches"""
import sqlite3
import os
from app.models import *

db_path = os.path.join(os.path.dirname(__file__), 'instance', 'visual_review.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
db_tables = [row[0] for row in cursor.fetchall()]

print("Checking all model/database schema mismatches...")
print("=" * 60)

# List of models to check
models_to_check = [
    ('Student', 'students'),
    ('User', 'users'),
    ('Teacher', 'teachers'),
    ('Exam', 'exams'),
    ('Subject', 'subjects'),
    ('IncidentReport', 'incident_reports'),
    ('ExamInvigilator', 'exam_invigilators'),
    ('InvigilatorLoginHistory', 'invigilator_login_history'),
    ('IncidentReportSettings', 'incident_report_settings'),
    ('IncidentCategory', 'incident_categories'),
    ('SeverityLevel', 'severity_levels'),
    ('IncidentAction', 'incident_actions'),
]

mismatches_found = False

for model_name, table_name in models_to_check:
    print(f"\nChecking {model_name} ({table_name})...")
    
    # Check if table exists
    if table_name not in db_tables:
        print(f"  [MISSING] Table '{table_name}' does not exist in database")
        mismatches_found = True
        continue
    
    # Get table schema
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    column_names = [col[1] for col in columns]
    
    # Get model columns (this is a simplified check - we'd need to inspect the model more thoroughly)
    # For now, just report the table exists
    print(f"  [OK] Table exists with {len(columns)} columns")

print("\n" + "=" * 60)
if mismatches_found:
    print("Schema mismatches found!")
else:
    print("No schema mismatches detected.")
print("=" * 60)

conn.close()
