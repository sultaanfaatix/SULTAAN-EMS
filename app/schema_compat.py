from sqlalchemy import inspect, text

from . import db


def ensure_schema_compatibility():
    """Add missing production columns safely without dropping or rewriting data."""
    inspector = inspect(db.engine)
    dialect = db.engine.dialect.name

    add_column_if_missing("users", "permissions", column_sql(dialect, "permissions", "TEXT"))
    add_column_if_missing("students", "phone", column_sql(dialect, "phone", "VARCHAR(40)"))
    add_column_if_missing("students", "level", column_sql(dialect, "level", "VARCHAR(80)"))
    add_column_if_missing("students", "section", column_sql(dialect, "section", "VARCHAR(80)"))


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
