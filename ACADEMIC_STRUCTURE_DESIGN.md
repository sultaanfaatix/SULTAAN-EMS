# Academic Structure Redesign - Implementation Plan

## Current Structure Analysis

### Existing Models
- `SchoolClass` - Flat structure with only name and description
- `Student` - Has class_id, level (string), section (string) - inconsistent hierarchy
- `Subject` - Flat structure, not level-specific
- `Teacher` - Has school_level enum but not integrated with academic structure
- `AcademicYear` - Separate from class structure

### Problems
1. No proper academic hierarchy
2. Level, class, and section are mixed inconsistently
3. Subjects not tied to academic levels
4. Teacher assignments don't respect academic structure
5. No centralized management of academic structure

## New Structure Design

### Hierarchy
```
School
├── AcademicLevel (Kindergarten, Lower Primary, Middle Primary, Secondary)
│   └── Class (Grade 1, Grade 2, Form 1, Form 2, etc.)
│       └── Section (A, B, C, etc.)
```

### New Models

#### AcademicLevel
- Represents the academic level (Kindergarten, Lower Primary, Middle Primary, Secondary)
- Sort order for display
- Active status

#### Class
- Represents the grade/form within an academic level
- Belongs to an AcademicLevel
- Name (Grade 1, Form 1, etc.)
- Sort order within level
- Active status

#### Section
- Represents sections within a class
- Belongs to a Class
- Name (A, B, C, etc.)
- Sort order
- Active status

### Updated Models

#### Student
- Add academic_level_id (FK to AcademicLevel)
- Add class_id (FK to new Class model - rename existing to school_class_id for migration)
- Add section_id (FK to Section)
- Keep existing level, section fields for backward compatibility during migration

#### Subject
- Add academic_level_id (FK to AcademicLevel)
- Make subjects level-specific

#### Teacher
- Update assignments to use new academic structure
- Add academic_level assignments
- Update class assignments to use new Class model
- Add section assignments

#### Exam
- Add academic_level_id
- Add class_id (new Class model)
- Add section_id

#### Result
- Keep existing structure (links to Student, Exam, Subject)
- Student will have new hierarchy, so results inherit it

## Migration Strategy

### Phase 1: Create New Models
1. Add AcademicLevel model
2. Add Class model (rename existing SchoolClass to LegacySchoolClass temporarily)
3. Add Section model
4. Update Subject model with academic_level_id

### Phase 2: Migrate Data
1. Create default academic levels (Kindergarten, Lower Primary, Middle Primary, Secondary)
2. Analyze existing SchoolClass data to determine appropriate academic levels
3. Create Class records from existing SchoolClass data
4. Create Section records (default to Section A for existing data)
5. Update Student records with new foreign keys
6. Update Subject records with academic_level_id

### Phase 3: Update Foreign Keys
1. Update Student model to use new Class and Section
2. Update Teacher assignment tables
3. Update Exam model
4. Update AttendanceRecord model
5. Update IdCardIssue model

### Phase 4: Update Application Code
1. Update Admin routes for academic structure management
2. Update Student registration forms
3. Update Teacher assignment forms
4. Update Examination module
5. Update Result entry
6. Update Reports module
7. Update Student search
8. Update Teacher Portal
9. Update templates

### Phase 5: Cleanup
1. Remove deprecated fields after verification
2. Drop legacy tables if safe
3. Update documentation

## Backward Compatibility

During migration:
- Keep existing fields with _legacy suffix
- Add new fields alongside existing ones
- Use database triggers or application logic to sync during transition
- Allow both old and new structures to work temporarily

After verification:
- Remove legacy fields
- Update all code to use new structure exclusively

## Data Preservation

- All existing student IDs preserved
- All existing teacher IDs preserved
- All existing result data preserved
- All existing report data preserved
- No data loss during migration

## Testing Requirements

1. Test student registration with new hierarchy
2. Test teacher assignment with new hierarchy
3. Test examination creation with new hierarchy
4. Test result entry with new hierarchy
5. Test reports with new hierarchy
6. Test student search with new hierarchy
7. Test teacher portal with new hierarchy
8. Verify all existing data is accessible
9. Verify Render and Railway compatibility
