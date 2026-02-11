import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")
    
    # Use PostgreSQL if DATABASE_URL is provided (Render), otherwise SQLite
    if os.environ.get("DATABASE_URL"):
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    else:
        SQLALCHEMY_DATABASE_URI = "sqlite:///employee.db"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
