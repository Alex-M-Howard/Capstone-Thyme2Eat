import os

from flask import Flask, redirect, url_for

from .db import connect_to_db, db
from .models.favorites_model import Favorite
from .models.joke_model import Joke
from .models.meal_model import Meal
from .models.user_model import User
from .routes.meal_routes.meal_routes import app_meal
from .routes.user_routes.user_routes import app_user

CURRENT_USER_ID = 'current_user'

def create_app(*args, **kwargs):
    # Create Flask app
    app = Flask(__name__)
    
    # Configure Setup
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL') 
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
    
    # Connect to DB
    connect_to_db(app)
    
    # Register routing blueprints
    app.register_blueprint(app_user)
    app.register_blueprint(app_meal)
    
    # Handle visit to app
    @app.route('/')
    def home():
        """ Go to User Routes where login/sign up or Profile will be loaded"""
        
        return redirect(url_for('app_user.home'))
    
    return app
