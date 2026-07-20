"""
Add indexes to GradeScale table for performance optimization
This migration adds indexes to frequently queried columns in the GradeScale table
to improve performance of grade lookups in analytics and other operations.
"""

from alembic import op
import sqlalchemy as sa


def upgrade():
    # Add indexes to GradeScale table
    op.create_index('idx_grade_scale_exam_id', 'grade_scales', ['exam_id'])
    op.create_index('idx_grade_scale_min_score', 'grade_scales', ['min_score'])
    op.create_index('idx_grade_scale_max_score', 'grade_scales', ['max_score'])
    op.create_index('idx_grade_scale_is_active', 'grade_scales', ['is_active'])


def downgrade():
    # Remove indexes from GradeScale table
    op.drop_index('idx_grade_scale_is_active', 'grade_scales')
    op.drop_index('idx_grade_scale_max_score', 'grade_scales')
    op.drop_index('idx_grade_scale_min_score', 'grade_scales')
    op.drop_index('idx_grade_scale_exam_id', 'grade_scales')
