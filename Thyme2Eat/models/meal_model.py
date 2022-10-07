from ..db import db

from ..models.favorites_model import Favorite


class Meal(db.Model):
    """ 
            MEAL MODEL
    ID                   : Primary Key
    Title                : Text
    Image URL            : Text 
    Servings             : Integer
    Time                 : Float
    Diets                : Text
    analyzedInstructions : Text -> JSON string
    nutrition_url        : Text
    """

    __tablename__ = 'meals'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text)
    servings = db.Column(db.Integer, nullable=False)
    nutrition_url = db.Column(db.Text)
    analyzedInstructions = db.Column(db.Text)
    meal_type = db.Column(db.Text,)
    time = db.Column(db.Float, nullable=False,)
    diets = db.Column(db.Text, nullable=False,)
    
    
    def __repr__(self):
        return f"<Meal #{self.id}: {self.title}>"
