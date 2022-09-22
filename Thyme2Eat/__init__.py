# flask --app Thyme2Eat --debug run
# https://realpython.com/flask-blueprint/
# Use url_for for redirects, render_templates otherwise
import os

from flask import Flask
from .routes import routes

def create_app(test_config=None):
    # Create Flask app and configure app
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='SECRET',
        DATABASE=os.path.join(app.instance_path, 'dinnerthyme.postgresql')
    )

    # Config Setup
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///thyme2eat"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # TODO Create environment variable for secret key when Done
    app.config["SECRET_KEY"] = "SECRET"
    
    # Create instance folder if Not exist
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Link app to routes
    app.register_blueprint(routes)
    
    return app
