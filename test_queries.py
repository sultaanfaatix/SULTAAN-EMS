"""Test script to verify all IncidentReport queries execute without errors"""
import sys
sys.path.insert(0, '.')

from app import create_app, db
from app.models import IncidentReport, Student, ExamInvigilator

app = create_app()

with app.app_context():
    print("Testing IncidentReport queries...")
    print("=" * 60)
    
    try:
        # Test count query
        count = IncidentReport.query.count()
        print(f"[OK] IncidentReport.count(): {count}")
    except Exception as e:
        print(f"[ERROR] IncidentReport.count(): {e}")
    
    try:
        # Test all query
        reports = IncidentReport.query.all()
        print(f"[OK] IncidentReport.query.all(): {len(reports)} records")
    except Exception as e:
        print(f"[ERROR] IncidentReport.query.all(): {e}")
    
    try:
        # Test filter query
        pending = IncidentReport.query.filter_by(status='Pending Review').all()
        print(f"[OK] IncidentReport.filter_by(status='Pending Review'): {len(pending)} records")
    except Exception as e:
        print(f"[ERROR] IncidentReport.filter_by(status='Pending Review'): {e}")
    
    try:
        # Test join with Student
        reports_with_student = IncidentReport.query.join(Student).all()
        print(f"[OK] IncidentReport.join(Student): {len(reports_with_student)} records")
    except Exception as e:
        print(f"[ERROR] IncidentReport.join(Student): {e}")
    
    try:
        # Test join with ExamInvigilator
        reports_with_invigilator = IncidentReport.query.join(ExamInvigilator).all()
        print(f"[OK] IncidentReport.join(ExamInvigilator): {len(reports_with_invigilator)} records")
    except Exception as e:
        print(f"[ERROR] IncidentReport.join(ExamInvigilator): {e}")
    
    try:
        # Test relationship access
        for report in IncidentReport.query.limit(5).all():
            _ = report.student
            _ = report.category
            _ = report.severity
            _ = report.invigilator
        print("[OK] Relationship access (student, category, severity, invigilator)")
    except Exception as e:
        print(f"[ERROR] Relationship access: {e}")
    
    try:
        # Test invigilator relationship
        invigilator = ExamInvigilator.query.first()
        if invigilator:
            _ = invigilator.submitted_reports.all()
            print("[OK] ExamInvigilator.submitted_reports relationship")
        else:
            print("[SKIP] ExamInvigilator.submitted_reports (no invigilators in DB)")
    except Exception as e:
        print(f"[ERROR] ExamInvigilator.submitted_reports: {e}")
    
    print("\n" + "=" * 60)
    print("All IncidentReport query tests completed!")
    print("=" * 60)
