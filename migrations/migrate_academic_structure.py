"""
Academic Structure Migration Script

This script migrates the existing flat academic structure to the new hierarchical structure:
- AcademicLevel -> AcademicClass -> AcademicSection

It preserves all existing data and maintains backward compatibility.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import (
    AcademicLevel, AcademicClass, AcademicSection, 
    Student, Subject, SchoolClass
)

def migrate_academic_structure():
    """Migrate existing data to new academic hierarchy"""
    app = create_app()
    
    with app.app_context():
        print("=== Starting Academic Structure Migration ===")
        
        # Step 1: Create default academic levels
        print("\nStep 1: Creating default academic levels...")
        default_levels = [
            ("Kindergarten", 1),
            ("Lower Primary", 2),
            ("Middle Primary", 3),
            ("Secondary", 4),
        ]
        
        level_map = {}
        for name, sort_order in default_levels:
            level = AcademicLevel.query.filter_by(name=name).first()
            if not level:
                level = AcademicLevel(name=name, sort_order=sort_order, is_active=True)
                db.session.add(level)
                db.session.flush()
            level_map[name] = level.id
            print(f"  - {name} (ID: {level.id})")
        
        db.session.commit()
        
        # Step 2: Analyze existing SchoolClass data and create AcademicClass records
        print("\nStep 2: Migrating SchoolClass to AcademicClass...")
        school_classes = SchoolClass.query.all()
        
        class_mapping = {}  # Maps old school_class_id to new academic_class_id
        
        for school_class in school_classes:
            # Determine appropriate academic level based on class name
            level_id = determine_level_for_class(school_class.name, level_map)
            
            # Check if AcademicClass already exists
            existing_class = AcademicClass.query.filter_by(
                academic_level_id=level_id,
                name=school_class.name
            ).first()
            
            if existing_class:
                class_mapping[school_class.id] = existing_class.id
                print(f"  - {school_class.name} -> Existing AcademicClass ID {existing_class.id} (Level ID {level_id})")
            else:
                # Create AcademicClass
                academic_class = AcademicClass(
                    academic_level_id=level_id,
                    name=school_class.name,
                    sort_order=0,
                    is_active=True
                )
                db.session.add(academic_class)
                db.session.flush()
                
                class_mapping[school_class.id] = academic_class.id
                print(f"  - {school_class.name} -> New AcademicClass ID {academic_class.id} (Level ID {level_id})")
        
        db.session.commit()
        
        # Step 3: Create default sections for each class
        print("\nStep 3: Creating default sections...")
        section_mapping = {}  # Maps (academic_class_id, section_name) to section_id
        
        for academic_class in AcademicClass.query.all():
            # Check if Section A already exists
            existing_section = AcademicSection.query.filter_by(
                academic_class_id=academic_class.id,
                name="A"
            ).first()
            
            if existing_section:
                section_mapping[(academic_class.id, "A")] = existing_section.id
                print(f"  - Existing Section A for {academic_class.name} (ID: {existing_section.id})")
            else:
                # Create Section A as default
                section = AcademicSection(
                    academic_class_id=academic_class.id,
                    name="A",
                    sort_order=1,
                    is_active=True
                )
                db.session.add(section)
                db.session.flush()
                section_mapping[(academic_class.id, "A")] = section.id
                print(f"  - New Section A for {academic_class.name} (ID: {section.id})")
        
        db.session.commit()
        
        # Step 4: Update Student records with new hierarchy
        print("\nStep 4: Updating Student records...")
        students = Student.query.all()
        
        for student in students:
            if student.class_id and student.class_id in class_mapping:
                student.academic_class_id = class_mapping[student.class_id]
                
                # Determine section based on existing section field or default to A
                section_name = student.section if student.section else "A"
                if (student.academic_class_id, section_name) not in section_mapping:
                    # Create section if it doesn't exist
                    section = AcademicSection(
                        academic_class_id=student.academic_class_id,
                        name=section_name,
                        sort_order=len(section_mapping) + 1,
                        is_active=True
                    )
                    db.session.add(section)
                    db.session.flush()
                    section_mapping[(student.academic_class_id, section_name)] = section.id
                
                student.academic_section_id = section_mapping[(student.academic_class_id, section_name)]
                
                # Set academic_level from class
                academic_class = AcademicClass.query.get(student.academic_class_id)
                if academic_class:
                    student.academic_level_id = academic_class.academic_level_id
                
                print(f"  - Student {student.student_code}: Level {student.academic_level_id}, Class {student.academic_class_id}, Section {student.academic_section_id}")
        
        db.session.commit()
        
        # Step 5: Update Subject records with academic_level_id
        print("\nStep 5: Updating Subject records...")
        subjects = Subject.query.all()
        
        # Default subjects to Secondary level if not specified
        secondary_level_id = level_map.get("Secondary")
        
        for subject in subjects:
            if subject.academic_level_id is None:
                subject.academic_level_id = secondary_level_id
                print(f"  - {subject.name} -> Level ID {secondary_level_id}")
        
        db.session.commit()
        
        # Step 6: Migrate teacher_classes table to reference academic_classes
        print("\nStep 6: Migrating teacher_classes table...")
        from sqlalchemy import text
        try:
            # Check if teacher_classes table exists and has data
            result = db.session.execute(text("SELECT COUNT(*) FROM teacher_classes")).scalar()
            print(f"Existing teacher_classes records: {result}")
            
            if result > 0:
                # Create mapping from school_classes to academic_classes
                school_to_academic = {}
                for school_class in SchoolClass.query.all():
                    academic_class = AcademicClass.query.filter_by(name=school_class.name).first()
                    if academic_class:
                        school_to_academic[school_class.id] = academic_class.id
                
                # Migrate teacher_classes records
                migrated_count = 0
                teacher_class_records = db.session.execute(text("SELECT teacher_id, class_id FROM teacher_classes")).all()
                
                for teacher_id, old_class_id in teacher_class_records:
                    if old_class_id in school_to_academic:
                        new_class_id = school_to_academic[old_class_id]
                        # Update the record
                        db.session.execute(
                            text("UPDATE teacher_classes SET class_id = :new_id WHERE teacher_id = :teacher_id AND class_id = :old_id"),
                            {"new_id": new_class_id, "teacher_id": teacher_id, "old_id": old_class_id}
                        )
                        migrated_count += 1
                
                db.session.commit()
                print(f"Migrated {migrated_count} teacher_classes records")
        except Exception as e:
            print(f"Teacher classes migration skipped or failed: {e}")
            db.session.rollback()
        
        print("\n=== Migration Complete ===")
        print(f"  - Academic Levels: {AcademicLevel.query.count()}")
        print(f"  - Academic Classes: {AcademicClass.query.count()}")
        print(f"  - Academic Sections: {AcademicSection.query.count()}")
        print(f"  - Students updated: {Student.query.filter(Student.academic_class_id.isnot(None)).count()}")
        print(f"  - Subjects updated: {Subject.query.filter(Subject.academic_level_id.isnot(None)).count()}")


def determine_level_for_class(class_name, level_map):
    """Determine appropriate academic level based on class name"""
    class_name_lower = class_name.lower()
    
    # Kindergarten indicators
    if any(kw in class_name_lower for kw in ['kg', 'kindergarten', 'nursery', 'reception']):
        return level_map.get("Kindergarten", level_map.get("Lower Primary"))
    
    # Lower Primary indicators (Grades 1-4)
    if any(kw in class_name_lower for kw in ['grade 1', 'grade 2', 'grade 3', 'grade 4', 'g1', 'g2', 'g3', 'g4', 'class 1', 'class 2', 'class 3', 'class 4']):
        return level_map.get("Lower Primary")
    
    # Middle Primary indicators (Grades 5-8)
    if any(kw in class_name_lower for kw in ['grade 5', 'grade 6', 'grade 7', 'grade 8', 'g5', 'g6', 'g7', 'g8', 'class 5', 'class 6', 'class 7', 'class 8']):
        return level_map.get("Middle Primary")
    
    # Secondary indicators (Forms 1-4, Grade 9-12)
    if any(kw in class_name_lower for kw in ['form 1', 'form 2', 'form 3', 'form 4', 'f1', 'f2', 'f3', 'f4', 'grade 9', 'grade 10', 'grade 11', 'grade 12', 'g9', 'g10', 'g11', 'g12', 'secondary', 'high school']):
        return level_map.get("Secondary")
    
    # Default to Secondary if no match
    return level_map.get("Secondary", level_map.get("Middle Primary"))


if __name__ == "__main__":
    migrate_academic_structure()
