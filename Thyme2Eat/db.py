from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_to_db(app):
    """Connect to DB and create tables if not exist"""
    
    db.app = app
    db.init_app(app)
    db.create_all()