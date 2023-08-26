import random

import requests
from flask import g

from ...db import db
from ...models.favorites_model import Favorite
from ...models.joke_model import Joke
from ...models.user_model import User
from ..meal_routes.meal_functions import SPOONACULAR_API_KEY

REGISTER_USER_API = 'https://api.spoonacular.com/users/connect'

def retrieve_user_saved_meals(user_id):
    """Retrieve User's saved meals from DB"""
    
    user = User.query.get(user_id)
    favorites = [{"title":meal.title, "id":meal.id, "image":meal.image, "meal_type":meal.meal_type} for meal in user.favorites]

    return favorites


def get_random_joke():
    """Retrieve random joke from DB"""
    
    jokes = Joke.query.all()
    
    return random.choice(jokes)

    
