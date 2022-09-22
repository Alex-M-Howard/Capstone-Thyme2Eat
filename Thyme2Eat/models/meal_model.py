""" 
        MEAL MODEL
  ID         : Primary Key
  Title      : Text
  Summary    : Text
  Image URL  : Text 
  Servings   : Integer
  Time       : Float
  Diets      : Text
"""

from ..db import db


class Meal(db.Model):
    """Saved meal in DB"""

    __tablename__ = 'meals'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    title = db.Column(
        db.Text,
        nullable=False,
    )

    summary = db.Column(
        db.Text,
        nullable=False,
    )

    image_url = db.Column(
        db.Text,
    )

    servings = db.Column(
        db.Integer,
        nullable=False,
    )

    # TODO CHECK API RETURN FOR FLOAT/INT
    time = db.Column(
        db.Float,
        nullable=False,
    )
    
    diets = db.Column(
        db.Text,
        nullable=False,
    )
    
  
    def __repr__(self):
        return f"<User #{self.id}: {self.title} - {self.summary}>"
