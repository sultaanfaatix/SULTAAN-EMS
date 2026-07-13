"""Script to check database schema and compare with models"""
import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'instance', 'visual_review.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get the schema of incident_reports table
cursor.execute("PRAGMA table_info(incident_reports)")
columns = cursor.fetchall()

print("Current incident_reports table schema:")
print("-" * 60)
for col in columns:
    print(f"  {col[1]}: {col[2]} {'(PK)' if col[5] else ''}")

print("\n" + "=" * 60)
print("Expected columns from model:")
print("-" * 60)
expected_columns = [
    "id", "report_number", "student_id", "teacher_id", "user_id", "invigilator_id",
    "exam_id", "subject_id", "category_id", "severity_id", "exam_room",
    "incident_date", "incident_time", "description", "actions_taken",
    "status", "reviewed_by_id", "reviewed_at", "review_notes",
    "created_at", "updated_at"
]
for col in expected_columns:
    print(f"  {col}")

print("\n" + "=" * 60)
print("Missing columns:")
print("-" * 60)
current_cols = [col[1] for col in columns]
missing = [col for col in expected_columns if col not in current_cols]
if missing:
    for col in missing:
        print(f"  {col}")
else:
    print("  None")

conn.close()
