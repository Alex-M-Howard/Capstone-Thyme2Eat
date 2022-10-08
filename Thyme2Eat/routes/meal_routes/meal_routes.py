from flask import Blueprint, render_template, flash, redirect, request, url_for, g, jsonify
from sqlalchemy.exc import IntegrityError

from ...models.meal_model import Meal
from ...models.user_model import User

from .meal_functions import *

# Create blueprint and custom routes
app_meal = Blueprint(
    'app_meal',
    __name__,
    static_folder='../../static',
    template_folder='templates',
    url_prefix='/meals'
    )


@app_meal.route('/random', methods=["GET"])
def get_random_meal():
    """ Show HTML for random meal. AJAX will run API request """
    
    return render_template('random_meal.html')
      
@app_meal.route(f'/recipe/<int:meal_id>', methods=["GET"])
def show_recipe(meal_id):
    """Show a recipe with instructions and nutrition facts"""

    recipe = retrieve_meal_from_db(meal_id)
    
    if recipe == None: 
        recipe = get_recipe(meal_id)
        nutrition = get_nutrition(meal_id)
    else:
        nutrition = recipe.nutrition_url
    
    similar = get_similar_recipes(meal_id)
    
    return render_template('show_recipe.html', recipe=recipe, nutrition=nutrition, similar=similar)
    
@app_meal.route('/<int:meal_id>/save', methods=["POST"])
def save_recipe(meal_id):
    """ Save recipe to User's favorites. If not in database, add in"""
    
    meal = retrieve_meal_from_db(meal_id)
       
    if meal == None: 
        meal = add_meal_to_db(meal_id)   

    add_meal_to_favorites(meal_id)
    return jsonify({"result": "added"}), 200

@app_meal.route('/<int:meal_id>/remove', methods=["DELETE"])
def remove_recipe(meal_id):
    """ Delete recipe from User's favorites"""
    
    remove_meal_from_favorites(meal_id)
    
    return jsonify({"result": "favorite deleted"})

@app_meal.route('/<int:meal_id>/print')
def print_recipe(meal_id):
    """Bring up printable version of recipe for user"""
    
    recipe = get_recipe(meal_id)
    nutrition = get_nutrition(meal_id)

    return render_template('printable_recipe.html', recipe=recipe, nutrition=nutrition)

@app_meal.route('/search')
def search():
    """Search for query in API"""
    
    query = request.args["query"]
    search_results = search_meals(query)
      
    return render_template('search.html', search_results=search_results)
