-- Execute this SQL on your Render MySQL Console to verify the fix

-- Check if invigilator_id column exists
SHOW COLUMNS FROM incident_reports;

-- Verify the table structure
SHOW CREATE TABLE incident_reports;

-- Check if exam_invigilators table exists
SHOW TABLES LIKE 'exam_invigilators';
