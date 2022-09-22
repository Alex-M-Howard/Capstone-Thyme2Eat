# TO RUN APP -> flask --app Thyme2Eat --debug run
import os

from flask import Flask

from .user_routes.user_routes import app_user
#from .meal_routes.meal_routes import app_meal -> Not implemented yet

from .models.meal_model import Meal
from .models.user_model import User

from .db import connect_to_db, db

API_KEY = '25bf790109054f9387a17986d94ebcfb'

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
    
    return app
