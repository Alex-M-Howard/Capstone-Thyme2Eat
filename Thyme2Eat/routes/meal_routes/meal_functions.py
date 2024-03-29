import json
import os

import requests
from flask import g

from ...db import db
from ...models.favorites_model import Favorite
from ...models.meal_model import Meal
from ...models.user_model import User

SPOONACULAR_API_KEY = os.environ.get('API_KEY') 
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
    
    ingredients = json.dumps(recipe["extendedIngredients"])
    instructions = json.dumps(recipe["analyzedInstructions"])

    new_meal = Meal(
        id=meal_id, 
        title=recipe['title'], 
        image=recipe['image'], 
        servings=recipe['servings'], 
        time=recipe['readyInMinutes'], 
        diets=recipe['diets'], 
        analyzedInstructions=instructions,
        extendedIngredients=ingredients,
        meal_type=recipe['dishTypes'],
        nutrition_url=nutrition_url)
    
    db.session.add(new_meal)
    db.session.commit()

    return new_meal

def retrieve_meal_from_db(meal_id):
    """Get meal from database"""
    
    meal = Meal.query.get(meal_id)
    
    if meal:
        parsed_ingredients = json.loads(meal.extendedIngredients)
        meal.extendedIngredients = parsed_ingredients
        
        parsed_instructions = json.loads(meal.analyzedInstructions)
        meal.analyzedInstructions = parsed_instructions
        
        return meal
    
    else:
        return None

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
    
    favorited_by_others = Favorite.query.filter_by(meal_id=meal_id).all()
    
    if not favorited_by_others:
        remove_meal_from_db(meal_id)
    
    return
        
def search_meals(query="", diet="", intolerances="", type="", number=12, sort="", instructionsRequired="true"):
    """Find meals based on user input"""
    
    params = {
        "apiKey": SPOONACULAR_API_KEY,
        "query": query,
        "number": number,
        "diet": diet,
        "intolerances": intolerances,
        "type": type,
        "sort": sort,
        "instructionsRequired": instructionsRequired
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
    
    if meal:
        similar = get_recipe(meal[0]['id'])
        return None if similar['id'] == meal_id else similar
    else:
        return None

def remove_meal_from_db(meal_id):
    """Remove meal from database"""
    
    meal = Meal.query.get(meal_id)
    db.session.delete(meal)
    db.session.commit()
       
    return
