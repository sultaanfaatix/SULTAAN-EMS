from sqlalchemy import inspect, text

from . import db


def ensure_schema_compatibility():
    """Add missing production columns safely without dropping or rewriting data."""
    inspector = inspect(db.engine)
    dialect = db.engine.dialect.name

    add_column_if_missing("users", "permissions", column_sql(dialect, "permissions", "TEXT"))
    add_column_if_missing("users", "photo_path", column_sql(dialect, "photo_path", "VARCHAR(255)"))
    add_column_if_missing("students", "phone", column_sql(dialect, "phone", "VARCHAR(40)"))
    add_column_if_missing("students", "level", column_sql(dialect, "level", "VARCHAR(80)"))
    add_column_if_missing("students", "section", column_sql(dialect, "section", "VARCHAR(80)"))
    add_column_if_missing("results", "grade_override", column_sql(dialect, "grade_override", "VARCHAR(10)"))
    add_column_if_missing("results", "comment", column_sql(dialect, "comment", "VARCHAR(255)"))
    widen_varchar_if_needed("results", "grade_override", 20)
    widen_varchar_if_needed("grade_scales", "grade", 20, nullable=False)
    add_column_if_missing("grade_scales", "grade_point", column_sql(dialect, "grade_point", "DECIMAL(4,2) NOT NULL DEFAULT 0"))
    add_column_if_missing("grade_scales", "is_pass", column_sql(dialect, "is_pass", "BOOLEAN NOT NULL DEFAULT TRUE"))
    add_column_if_missing("grade_scales", "badge_color", column_sql(dialect, "badge_color", "VARCHAR(20) NOT NULL DEFAULT '#10b981'"))
    add_column_if_missing("grade_scales", "text_color", column_sql(dialect, "text_color", "VARCHAR(20) NOT NULL DEFAULT '#ffffff'"))
    add_column_if_missing("grade_scales", "background_color", column_sql(dialect, "background_color", "VARCHAR(20) NOT NULL DEFAULT '#ecfdf5'"))
    add_column_if_missing("grade_scales", "border_color", column_sql(dialect, "border_color", "VARCHAR(20) NOT NULL DEFAULT '#10b981'"))
    add_column_if_missing("grade_scales", "sort_order", column_sql(dialect, "sort_order", "INTEGER NOT NULL DEFAULT 0"))
    add_column_if_missing("grade_scales", "is_active", column_sql(dialect, "is_active", "BOOLEAN NOT NULL DEFAULT TRUE"))


def add_column_if_missing(table, column, ddl):
    inspector = inspect(db.engine)
    existing = {row["name"] for row in inspector.get_columns(table)}
    if column in existing:
        return
    db.session.execute(text(f"ALTER TABLE {table} ADD COLUMN {ddl}"))
    db.session.commit()


def column_sql(dialect, name, type_sql):
    if dialect == "sqlite":
        return f"{name} {type_sql}"
    return f"{name} {type_sql}"


def widen_varchar_if_needed(table, column, length, nullable=True):
    inspector = inspect(db.engine)
    existing = {row["name"]: row for row in inspector.get_columns(table)}
    row = existing.get(column)
    if not row:
        return
    current_length = getattr(row["type"], "length", None)
    if current_length and current_length >= length:
        return
    dialect = db.engine.dialect.name
    if dialect == "mysql":
        null_sql = "NULL" if nullable else "NOT NULL"
        db.session.execute(text(f"ALTER TABLE {table} MODIFY COLUMN {column} VARCHAR({length}) {null_sql}"))
        db.session.commit()
