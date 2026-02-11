import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Database configuration
    _database_url = os.environ.get("DATABASE_URL")
    
    # Fix PostgreSQL URL format for SQLAlchemy
    if _database_url:
        if _database_url.startswith("postgres://"):
            _database_url = _database_url.replace("postgres://", "postgresql://", 1)
        SQLALCHEMY_DATABASE_URI = _database_url
    else:
        SQLALCHEMY_DATABASE_URI = "sqlite:///instance/employee.db"
