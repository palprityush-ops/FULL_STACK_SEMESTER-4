import os

def get_database_uri():
    """Get database URI, fixing PostgreSQL URL format if needed."""
    db_url = os.environ.get("DATABASE_URL")
    if db_url:
        # Fix PostgreSQL URL format for SQLAlchemy
        if db_url.startswith("postgres://"):
            db_url = db_url.replace("postgres://", "postgresql://", 1)
        return db_url
    return "sqlite:///instance/employee.db"

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")
    SQLALCHEMY_DATABASE_URI = get_database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
