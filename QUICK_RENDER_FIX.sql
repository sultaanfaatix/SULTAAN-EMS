-- Execute this SQL on your Render MySQL Console
-- This will add the missing invigilator_id column

-- Step 1: Add the invigilator_id column
ALTER TABLE incident_reports 
ADD COLUMN invigilator_id INT NULL 
AFTER user_id;

-- Step 2: Add index for performance
ALTER TABLE incident_reports 
ADD INDEX idx_incident_reports_invigilator_id (invigilator_id);

-- Step 3: Create exam_invigilators table (needed for foreign key)
CREATE TABLE IF NOT EXISTS exam_invigilators (
    id INT AUTO_INCREMENT PRIMARY KEY,
    invigilator_id VARCHAR(50) UNIQUE NOT NULL,
    username VARCHAR(80) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(180) NOT NULL,
    photo_path VARCHAR(255),
    mobile_number VARCHAR(40),
    role ENUM('Invigilator', 'Supervisor', 'Chief Invigilator', 'Administrator') DEFAULT 'Invigilator' NOT NULL,
    school VARCHAR(180),
    notes TEXT,
    status ENUM('Active', 'Inactive', 'Locked') DEFAULT 'Active' NOT NULL,
    is_active TINYINT(1) DEFAULT 1 NOT NULL,
    force_password_change TINYINT(1) DEFAULT 0 NOT NULL,
    active_from DATE,
    active_until DATE,
    last_login_at DATETIME,
    last_logout_at DATETIME,
    failed_login_attempts INT DEFAULT 0,
    locked_until DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_exam_invigilators_invigilator_id (invigilator_id),
    INDEX idx_exam_invigilators_username (username),
    INDEX idx_exam_invigilators_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Step 4: Add foreign key constraint
ALTER TABLE incident_reports 
ADD CONSTRAINT fk_incident_reports_invigilator_id 
FOREIGN KEY (invigilator_id) REFERENCES exam_invigilators(id) 
ON DELETE SET NULL;
