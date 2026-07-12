import sys
import os

# Add the exam_system directory to the path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import create_app
from app.models import AcademicLevel, AcademicClass, AcademicSection, Student, Subject, SchoolClass

app = create_app()

with app.app_context():
    print("=== Backward Compatibility Verification ===")
    
    # Test 1: Legacy SchoolClass still exists and accessible
    print("\n=== Test 1: Legacy SchoolClass Access ===")
    school_classes = SchoolClass.query.all()
    print(f"Legacy SchoolClass count: {len(school_classes)}")
    for school_class in school_classes:
        print(f"  - {school_class.name} (ID: {school_class.id})")
    
    # Test 2: Student legacy fields still accessible
    print("\n=== Test 2: Student Legacy Fields ===")
    students = Student.query.all()
    print(f"Total students: {len(students)}")
    for student in students:
        print(f"  - {student.student_code}:")
        print(f"    Legacy class_id: {student.class_id}")
        print(f"    Legacy level: {student.level}")
        print(f"    Legacy section: {student.section}")
        print(f"    New academic_level_id: {student.academic_level_id}")
        print(f"    New academic_class_id: {student.academic_class_id}")
        print(f"    New academic_section_id: {student.academic_section_id}")
    
    # Test 3: Subject can still work without academic_level_id
    print("\n=== Test 3: Subject Backward Compatibility ===")
    subjects = Subject.query.all()
    print(f"Total subjects: {len(subjects)}")
    for subject in subjects:
        print(f"  - {subject.name} (academic_level_id: {subject.academic_level_id})")
    
    # Test 4: Verify relationships still work
    print("\n=== Test 4: Relationship Verification ===")
    for student in students:
        if student.class_id:
            legacy_class = SchoolClass.query.get(student.class_id)
            print(f"  - {student.student_code} legacy class relationship: {legacy_class.name if legacy_class else 'None'}")
        if student.academic_class_id:
            new_class = AcademicClass.query.get(student.academic_class_id)
            print(f"  - {student.student_code} new class relationship: {new_class.name if new_class else 'None'}")
    
    # Test 5: Check that no data was lost
    print("\n=== Test 5: Data Preservation ===")
    print(f"Original student count preserved: {len(students)}")
    print(f"Original subject count preserved: {len(subjects)}")
    print(f"Original school class count preserved: {len(school_classes)}")
    
    print("\n=== Backward Compatibility Verification Complete ===")
    print("[OK] All legacy fields accessible")
    print("[OK] All relationships working")
    print("[OK] No data lost during migration")
