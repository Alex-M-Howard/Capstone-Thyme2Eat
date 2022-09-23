from flask import Blueprint, render_template, flash, redirect, request, url_for

import requests

SPOONACULAR_API_KEY = '25bf790109054f9387a17986d94ebcfb'
RECIPES_API = 'https://api.spoonacular.com/recipes'

# Searching the API
COMPLEX_SEARCH = 'complexSearch'
AUTOCOMPLETE_SEARCH = 'autocomplete'
FIND_BY_INGREDIENTS = 'findByIngredients'

# Recipe endpoints
INFO = 'information'
SIMILAR = 'similar'
NUTRITION_LABEL = 'nutritionLabel.png'

# Miscellaneous API endpoints
FOOD_JOKES_API = 'food/jokes/random'

app_meal = Blueprint(
    'app_meal',
    __name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/meals'
    )


@app_meal.route('/')
def home():
    return render_template('/home.html')


@app_meal.route('/random', methods=["GET", "POST"])
def get_random_meal():
    """ Retrieve and show a random meal with nutrition, ingredients, and directions """
    if request.method=="POST":
        r = request.form
        
        params = {
            "apiKey": SPOONACULAR_API_KEY,
            "diet": r["diet"],
            "intolerances": r["intolerances"],
            "type": r["type"],
            "number": 6,
            "sort": "random",
            "instructionsRequired": "true", 
        }

        response = requests.get(f"{RECIPES_API}/{COMPLEX_SEARCH}", params)
        meals = response.json()
                 
        return render_template('random_meal.html', meals=meals['results'])
    else:
        return render_template('random_meal.html')
    
    
@app_meal.route(f'/recipe/<int:meal_id>', methods=["GET"])
def show_recipe(meal_id):
    """Show a recipe with instructions and nutrition facts"""
    
    params = {
        "apiKey": SPOONACULAR_API_KEY,
        "id": meal_id
    }

    recipe = requests.get(f"{RECIPES_API}/{meal_id}/{INFO}", params)
    nutrition = requests.get(f"{RECIPES_API}/{meal_id}/{NUTRITION_LABEL}", params)
    
    return render_template('show_recipe.html', recipe=recipe.json(), nutrition=nutrition.url)
    