import json

from flask import g

from ...db import db

from ...models.meal_model import Meal
from ...models.user_model import User
from ...models.favorites_model import Favorite

import requests


SPOONACULAR_API_KEY = '25bf790109054f9387a17986d94ebcfb'#'1970c7ca2a3543389708d99f3a67d353' 
RECIPES_API = 'https://api.spoonacular.com/recipes'

# Searching the API
COMPLEX_SEARCH = 'complexSearch'             # 1 point + 0.01/recipe returned
FIND_BY_INGREDIENTS = 'findByIngredients'

# Recipe endpoints
INFO = 'information'                         # 1 point
SIMILAR = 'similar'                          # 1 point + 0.01/recipe returned
NUTRITION_LABEL = 'nutritionLabel.png'       # 1 point

# Miscellaneous API endpoints
FOOD_JOKES_API = 'food/jokes/random'         # 1 point

def get_recipe(meal_id):
    """Get recipe data --> Returns JSON"""
    
    params = {
        "apiKey": SPOONACULAR_API_KEY,
        "id": meal_id
    }

    recipe = requests.get(f"{RECIPES_API}/{meal_id}/{INFO}", params)
    
    return recipe.json()

def get_nutrition(meal_id):
    """ Get recipe nutrition --> Returns Image URL"""
    params = {
        "apiKey": SPOONACULAR_API_KEY,
        "id": meal_id
    }
    
    image = requests.get(f"{RECIPES_API}/{meal_id}/{NUTRITION_LABEL}", params)
    
    return image.url

def add_meal_to_db(meal_id):
    """Add meal to database"""

    recipe = get_recipe(meal_id)
    nutrition_url = get_nutrition(meal_id)
    
    instructions = json.dumps(recipe["analyzedInstructions"])
    
    new_meal = Meal(
        id=meal_id, 
        title=recipe['title'], 
        image_url=recipe['image'], 
        servings=recipe['servings'], 
        time=recipe['readyInMinutes'], 
        diets=recipe['diets'], 
        analyzedInstructions=instructions,
        meal_type=recipe['dishTypes'],
        nutrition_url=nutrition_url)
    
    db.session.add(new_meal)
    db.session.commit()

    return new_meal

def retrieve_meal_from_db(meal_id):
    """Get meal from database"""
    
    return Meal.query.get(meal_id)

def add_meal_to_favorites(meal_id):
    """Add meal to user's favorites"""
    
    user = User.query.get(g.user.id)
    
    favorite_meal = Favorite(user_id=user.id, meal_id=meal_id)
    
    db.session.add(favorite_meal)
    db.session.commit()
    
    return

def remove_meal_from_favorites(meal_id):
    """Remove meal from user's favorites"""
    
    favorite_meal = Favorite.query.filter_by(user_id=g.user.id, meal_id=meal_id).one()
    
    db.session.delete(favorite_meal)    
    db.session.commit()
    
    return

def search_meals(query):
    """Find meals based on user input"""
    
    params = {
        "apiKey": SPOONACULAR_API_KEY,
        "query": query,
        "number": 8
    }
    
    results = requests.get(f"{RECIPES_API}/{COMPLEX_SEARCH}", params)
    
    return results.json()

def get_similar_recipes(meal_id):
    """Fetch similar recipes when a user views a recipe"""

    params = {
        "apiKey": SPOONACULAR_API_KEY,
        "id": meal_id,
        "number": 1
    }

    meal = requests.get(f"{RECIPES_API}/{meal_id}/{SIMILAR}", params)  
    meal = meal.json()
    
    similar = get_recipe(meal[0]['id'])

    return similar
