import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")
    
    # Database configuration
    database_url = os.environ.get("DATABASE_URL")
    if database_url:
        # Fix PostgreSQL URL format for SQLAlchemy
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        SQLALCHEMY_DATABASE_URI = database_url
    else:
        # Use SQLite for local development
        SQLALCHEMY_DATABASE_URI = "sqlite:///instance/employee.db"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
