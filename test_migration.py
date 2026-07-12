"""
Test script to verify the academic structure migration
"""

from app import create_app, db
from app.models import AcademicLevel, AcademicClass, AcademicSection, Student, Subject

def test_migration():
    app = create_app()
    
    with app.app_context():
        print("=== Testing Academic Structure ===")
        
        print(f"\nAcademic Levels: {AcademicLevel.query.count()}")
        for level in AcademicLevel.query.order_by(AcademicLevel.sort_order).all():
            print(f"  - {level.name} (ID: {level.id}, Active: {level.is_active})")
        
        print(f"\nAcademic Classes: {AcademicClass.query.count()}")
        for cls in AcademicClass.query.order_by(AcademicClass.sort_order).all():
            print(f"  - {cls.name} (Level: {cls.academic_level.name}, ID: {cls.id}, Active: {cls.is_active})")
        
        print(f"\nAcademic Sections: {AcademicSection.query.count()}")
        for section in AcademicSection.query.order_by(AcademicSection.sort_order).all():
            print(f"  - {section.name} (Class: {section.academic_class.name}, ID: {section.id}, Active: {section.is_active})")
        
        print(f"\nStudents with new hierarchy: {Student.query.filter(Student.academic_class_id.isnot(None)).count()}")
        for student in Student.query.limit(5).all():
            print(f"  - {student.student_code}: Level {student.academic_level_id}, Class {student.academic_class_id}, Section {student.academic_section_id}")
        
        print(f"\nSubjects with level: {Subject.query.filter(Subject.academic_level_id.isnot(None)).count()}")
        for subject in Subject.query.limit(5).all():
            print(f"  - {subject.name} (Level ID: {subject.academic_level_id})")

if __name__ == "__main__":
    test_migration()
