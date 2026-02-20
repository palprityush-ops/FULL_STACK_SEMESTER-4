from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app


# Expose a package-level `app` so WSGI servers can import `app:app`.
# This keeps existing `run.py` and `wsgi.py` behaviour unchanged.
app = create_app()
