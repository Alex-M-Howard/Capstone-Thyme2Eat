# flask --app Thyme2Eat --debug run
# https://realpython.com/flask-blueprint/

import os

from flask import Flask
from .user_routes.user_routes import app_user
from .db import connect_to_db


def create_app(test_config=None):
    # Create Flask app and configure app
    
    app = Flask(__name__)
    
    # Config Setup
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///thyme2eat"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # TODO Create environment variable for secret key when Done
    app.config["SECRET_KEY"] = "SECRET"
    
    connect_to_db(app)
    
    # Register routing blueprints
    app.register_blueprint(app_user)
    
    return app
