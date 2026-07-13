"""
Run this script on Render to check the production database schema
Execute on Render: python check_render_schema.py
"""
import sys
from app import create_app, db
from sqlalchemy import text, inspect

app = create_app()

def check_render_schema():
    """Check the Render production database schema"""
    with app.app_context():
        print("=" * 70)
        print("RENDER PRODUCTION DATABASE SCHEMA CHECK")
        print("=" * 70)
        
        # Check database type
        db_url = db.engine.url
        print(f"\nDatabase URL: {db_url}")
        print(f"Database Type: {db_url.drivername}")
        print(f"Database Name: {db_url.database}")
        
        print("\n" + "=" * 70)
        print("SHOW CREATE TABLE incident_reports")
        print("=" * 70)
        
        try:
            with db.engine.connect() as conn:
                result = conn.execute(text("SHOW CREATE TABLE incident_reports"))
                row = result.fetchone()
                print("\n" + row[1])
        except Exception as e:
            print(f"\n[ERROR] Failed to get table structure: {e}")
            return False
        
        print("\n" + "=" * 70)
        print("CHECK FOR invigilator_id COLUMN")
        print("=" * 70)
        
        inspector = inspect(db.engine)
        columns = inspector.get_columns('incident_reports')
        
        invigilator_id_exists = False
        for col in columns:
            if col['name'] == 'invigilator_id':
                invigilator_id_exists = True
                print(f"\n[FOUND] invigilator_id column exists")
                print(f"  Type: {col['type']}")
                print(f"  Nullable: {col['nullable']}")
                print(f"  Default: {col['default']}")
                break
        
        if not invigilator_id_exists:
            print("\n[MISSING] invigilator_id column does NOT exist in incident_reports table")
            print("\nCurrent columns in incident_reports:")
            for col in columns:
                print(f"  - {col['name']}: {col['type']}")
        
        print("\n" + "=" * 70)
        print("CHECK FOR exam_invigilators TABLE")
        print("=" * 70)
        
        tables = inspector.get_table_names()
        if 'exam_invigilators' in tables:
            print("[OK] exam_invigilators table exists")
        else:
            print("[MISSING] exam_invigilators table does NOT exist")
        
        print("\n" + "=" * 70)
        print("RESULT")
        print("=" * 70)
        
        if invigilator_id_exists:
            print("\n[RESULT] invigilator_id column EXISTS in production database")
            print("The migration has been applied.")
            return True
        else:
            print("\n[RESULT] invigilator_id column MISSING from production database")
            print("The migration has NOT been applied.")
            print("\nYou must run: python apply_production_migration.py")
            return False

if __name__ == "__main__":
    try:
        success = check_render_schema()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n[FATAL ERROR] Schema check failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
