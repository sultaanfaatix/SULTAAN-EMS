# Render Production Database Fix - Step-by-Step Guide

## Current Situation

The Render production MySQL database is **missing the `invigilator_id` column** from the `incident_reports` table. This is causing the SQLAlchemy OperationalError when submitting incident reports.

## You Must Execute These Commands on Render

I cannot access your Render production database directly. You must execute these commands yourself.

## Step 1: Deploy the Fix Scripts to Render

Add these files to your repository and push to Render:

1. `check_render_schema.py` - Checks if invigilator_id column exists
2. `apply_production_migration.py` - Adds the missing column and tables
3. `verify_production_schema.py` - Verifies the migration was successful

## Step 2: Check the Current Schema

### Option A: Using Render Shell (Recommended)

1. Go to https://dashboard.render.com
2. Navigate to your web service
3. Click "Shell" (or "SSH")
4. Run:
   ```bash
   python check_render_schema.py
   ```

This will show you the current `SHOW CREATE TABLE incident_reports` output and confirm whether `invigilator_id` exists.

### Option B: Using Render MySQL Console

1. Go to https://dashboard.render.com
2. Navigate to your MySQL service
3. Click "Console"
4. Click "Open Console"
5. Run:
   ```sql
   SHOW CREATE TABLE incident_reports;
   ```

Look for `invigilator_id` in the output. If it's missing, proceed to Step 3.

## Step 3: Apply the Migration

### Option A: Using Python Script (Recommended)

In the Render Shell, run:
```bash
python apply_production_migration.py
```

This script will:
- Check if running on MySQL
- Add `invigilator_id` column to `incident_reports` table
- Create `exam_invigilators` table
- Create `invigilator_login_history` table
- Create `incident_report_settings` table
- Seed default settings
- Verify all changes

### Option B: Using Raw SQL

In the Render MySQL Console, run:

```sql
-- Add invigilator_id column
ALTER TABLE incident_reports 
ADD COLUMN invigilator_id INT NULL 
AFTER user_id;

-- Add index
ALTER TABLE incident_reports 
ADD INDEX idx_incident_reports_invigilator_id (invigilator_id);

-- Create exam_invigilators table
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

-- Add foreign key constraint
ALTER TABLE incident_reports 
ADD CONSTRAINT fk_incident_reports_invigilator_id 
FOREIGN KEY (invigilator_id) REFERENCES exam_invigilators(id) 
ON DELETE SET NULL;
```

## Step 4: Verify the Migration

In the Render Shell, run:
```bash
python verify_production_schema.py
```

Expected output:
```
[RESULT] SCHEMA VERIFICATION PASSED
The production database schema matches the SQLAlchemy models.
```

## Step 5: Test Incident Report Submission

1. Log in as an invigilator on your Render production site
2. Navigate to the incident report form
3. Fill out and submit an incident report
4. Verify:
   - ✅ No HTTP 500 error
   - ✅ Success message appears
   - ✅ Report is saved to database

## Step 6: Verify in Admin Panel

1. Log in as admin on your Render production site
2. Navigate to Admin Incident Management
3. Verify the submitted report appears

## What to Report Back

After completing these steps, please provide:

1. **Output of `SHOW CREATE TABLE incident_reports;`** (from Step 2)
2. **Output of `python check_render_schema.py`** (from Step 2)
3. **Output of `python apply_production_migration.py`** (from Step 3)
4. **Output of `python verify_production_schema.py`** (from Step 4)
5. **Confirmation that incident report submission works** (from Step 5)

## Troubleshooting

### Error: "Column invigilator_id already exists"

This is normal - the script checks before adding. Continue to verification.

### Error: "Foreign key constraint fails"

The exam_invigilators table must exist before adding the foreign key. The Python script handles this automatically.

### Error: "Access denied"

Verify your MySQL credentials in Render dashboard.

### Error: "Table doesn't exist"

The Python script creates missing tables automatically.

## Important Notes

- The migration scripts are **idempotent** - safe to run multiple times
- They will **not cause data loss**
- They will **not corrupt existing data**
- The scripts check for existing columns/tables before creating them

## Files to Deploy

Make sure these files are in your repository and deployed to Render:

1. `check_render_schema.py`
2. `apply_production_migration.py`
3. `verify_production_schema.py`
4. `migrations/mysql_migration.sql` (optional, for manual SQL execution)

## Code Changes Already Made

These code changes are already in your repository and should be deployed:

1. `app/routes_public.py` - Added `flash` import
2. `app/templates/invigilator/login.html` - Added CSRF token
3. `app/templates/invigilator/change_password.html` - Added CSRF token

These fix the CSRF errors that were also occurring.
