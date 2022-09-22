# TO RUN APP -> flask --app Thyme2Eat --debug run
import os

from flask import Flask

from .routes.user_routes.user_routes import app_user
from .routes.meal_routes.meal_routes import app_meal 
from .models.meal_model import Meal
from .models.user_model import User

from .db import connect_to_db, db



def create_app():
    # Create Flask app
    app = Flask(__name__)
    
    # Configure Setup
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///thyme2eat"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # TODO Create environment variable for secret key when Done
    app.config["SECRET_KEY"] = "SECRET"
    
    # Connect to DB
    connect_to_db(app)
    
    # Register routing blueprints -> https://realpython.com/flask-blueprint/
    app.register_blueprint(app_user)
    app.register_blueprint(app_meal)
    
    return app


