import sys
import os

# Add the exam_system directory to the path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import create_app
from app.models import AcademicLevel, AcademicClass, AcademicSection, Student, Subject

app = create_app()

with app.app_context():
    print("=== Academic Structure Verification ===")
    print(f"Academic Levels: {AcademicLevel.query.count()}")
    print(f"Academic Classes: {AcademicClass.query.count()}")
    print(f"Academic Sections: {AcademicSection.query.count()}")
    print(f"Students with new hierarchy: {Student.query.filter(Student.academic_class_id.isnot(None)).count()}")
    print(f"Subjects with level: {Subject.query.filter(Subject.academic_level_id.isnot(None)).count()}")
    
    print("\n=== Academic Levels ===")
    for level in AcademicLevel.query.all():
        print(f"  - {level.name} (ID: {level.id}, Sort: {level.sort_order}, Active: {level.is_active})")
    
    print("\n=== Academic Classes ===")
    for cls in AcademicClass.query.all():
        print(f"  - {cls.name} (Level: {cls.academic_level.name}, ID: {cls.id}, Sort: {cls.sort_order}, Active: {cls.is_active})")
    
    print("\n=== Academic Sections ===")
    for section in AcademicSection.query.all():
        print(f"  - {section.name} (Class: {section.academic_class.name}, ID: {section.id}, Sort: {section.sort_order}, Active: {section.is_active})")
    
    print("\n=== Students with New Hierarchy ===")
    for student in Student.query.filter(Student.academic_class_id.isnot(None)).all():
        print(f"  - {student.student_code}: Level={student.academic_level_id}, Class={student.academic_class_id}, Section={student.academic_section_id}")
    
    print("\n=== Subjects with Level ===")
    for subject in Subject.query.filter(Subject.academic_level_id.isnot(None)).all():
        print(f"  - {subject.name} (Level ID: {subject.academic_level_id})")
    
    print("\n=== Verification Complete ===")
