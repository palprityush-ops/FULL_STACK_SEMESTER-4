import os

def get_database_uri():
    """Get database URI, fixing PostgreSQL URL format if needed."""
    db_url = os.environ.get("DATABASE_URL")
    if db_url:
        # Fix PostgreSQL URL format for SQLAlchemy
        if db_url.startswith("postgres://"):
            db_url = db_url.replace("postgres://", "postgresql://", 1)
        return db_url
    # Use an absolute path for the local sqlite file to avoid relative-path
    # issues on different platforms (especially Windows).
    base_dir = os.path.abspath(os.path.dirname(__file__))
    instance_dir = os.path.join(base_dir, "instance")
    os.makedirs(instance_dir, exist_ok=True)
    db_path = os.path.join(instance_dir, "employee.db")
    # SQLAlchemy expects forward slashes in file URIs on Windows
    db_path_uri = db_path.replace("\\", "/")
    return f"sqlite:///{db_path_uri}"

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")
    SQLALCHEMY_DATABASE_URI = get_database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
