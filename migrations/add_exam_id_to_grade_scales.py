"""
Add exam_id column to grade_scales table

This migration adds a nullable exam_id foreign key to the grade_scales table,
allowing grade scales to be scoped per exam while preserving existing global
grade scales (exam_id IS NULL) as the fallback.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from sqlalchemy import text

def migrate_grade_scales():
    """Add exam_id column to grade_scales table"""
    app = create_app()
    
    with app.app_context():
        print("=== Adding exam_id column to grade_scales ===")
        
        # Check if column already exists
        inspector = db.inspect(db.engine)
        columns = [col['name'] for col in inspector.get_columns('grade_scales')]
        
        if 'exam_id' in columns:
            print("Column 'exam_id' already exists in grade_scales table. Skipping migration.")
            return
        
        # Add the column (SQLite requires separate statements)
        print("Adding exam_id column to grade_scales table...")
        db.session.execute(text("ALTER TABLE grade_scales ADD COLUMN exam_id INTEGER"))
        db.session.commit()
        
        # Verify the column was added
        columns = [col['name'] for col in inspector.get_columns('grade_scales')]
        if 'exam_id' in columns:
            print("[OK] Column 'exam_id' successfully added to grade_scales table")
            print(f"  Current columns: {', '.join(columns)}")
        else:
            print("[ERROR] Failed to add column 'exam_id'")
            db.session.rollback()
        
        print("\n=== Migration Complete ===")

if __name__ == "__main__":
    migrate_grade_scales()
