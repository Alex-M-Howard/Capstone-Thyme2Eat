from ..db import db


class Favorite(db.Model):
    """ 
        FAVORITES MODEL
    ID       : Primary Key
    USER ID  : Integer, Unique
    MEAL ID  : Integer, Unique
    """

    __tablename__ = 'favorites' 

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='cascade'))

    meal_id = db.Column(db.Integer, db.ForeignKey('meals.id', ondelete='cascade'), unique=True)
