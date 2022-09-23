from flask import Blueprint, render_template, flash, redirect, request, url_for

import requests
# Use url_for for redirects, render_templates otherwise

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
    
    
@app_meal.route(f'/recipe/<int:meal_id>', methods=["GET", "POST"])
def show_recipe(meal_id):
    print('welcome to here')
    
    return redirect(url_for('app_meal.home'))
    
    
    
"""

GET https://api.spoonacular.com/recipes/{id}/similar -> Get similar recipes
GET https://api.spoonacular.com/recipes/autocomplete -> Autocomplete search
GET https://api.spoonacular.com/recipes/{id}/information -> Get recipe info
GET https://api.spoonacular.com/recipes/findByIngredients -> Search by ingredients
GET https://api.spoonacular.com/recipes/{id}/ingredientWidget.json -> search by ingredient ID
GET https://api.spoonacular.com/recipes/{id}/nutritionWidget.json  -> Nutrition by ID
GET https://api.spoonacular.com/recipes/{id}/card -> recipe card

GET https://api.spoonacular.com/mealplanner/generate
GET https://api.spoonacular.com/mealplanner/{username}/shopping-list


Connect User
In order to call user-specific endpoints, you need to connect your app's users to spoonacular users.

Just call this endpoint with your user's information and you will get back a username and hash that you must save on your side. In future requests that you make on this user's behalf you simply pass their username and hash alongside your API key.

Read more about working with the meal planner.

POST https://api.spoonacular.com/users/connect



"""
