from flask import g 
import random
import requests

from ...db import db 

from ...models.user_model import User
from ...models.favorites_model import Favorite
from ...models.joke_model import Joke

from ..meal_routes.meal_functions import SPOONACULAR_API_KEY

REGISTER_USER_API = 'https://api.spoonacular.com/users/connect'

def retrieve_user_saved_meals(user_id):
    """Retrieve User's saved meals from DB"""
    
    user = User.query.get(user_id)
    favorites = [{"title":meal.title, "id":meal.id, "image_url":meal.image_url, "meal_type":meal.meal_type} for meal in user.favorites]

    return favorites


def get_random_joke():
    """Retrieve random joke from DB"""
    
    jokes = Joke.query.all()
    
    return random.choice(jokes)

def remove_saved_recipe(user_id, meal_id):
    """Remove recipe from user's DB"""
    
    saved = Favorite.query.filter_by(user_id=user_id, meal_id=meal_id).one()
    
    db.session.delete(saved)
    db.session.commit()
    
def connect_user_to_api():
    """Register user in Spoonacular API"""
    
    user = User.query.get(g.user.id)
    
    params = {
        "apiKey": SPOONACULAR_API_KEY,
        "username" : user.username,
        "email": user.email
    }
    print(user)
    response = requests.post(REGISTER_USER_API, params)
    print(response)
    response = response.json()
    print(response)
    user.api_username = response[0]["username"]
    user.api_password = response[0]["hash"]
    
    db.session.add(user)
    db.session.commit() 
    
    return user