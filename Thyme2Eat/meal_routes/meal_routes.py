from flask import Blueprint, render_template, flash, redirect, request
# Use url_for for redirects, render_templates otherwise

app_meal = Blueprint(
    'route',
    __name__,
    static_folder='static',
    template_folder='templates'
    )

@app_meal.route('/')
def home():
    return render_template('/home.html')

"""
GET https://api.spoonacular.com/recipes/complexSearch   -> Search Recipes
GET https://api.spoonacular.com/recipes/{id}/similar -> Get similar recipes
GET https://api.spoonacular.com/recipes/autocomplete -> Autocomplete search
GET https://api.spoonacular.com/recipes/{id}/information -> Get recipe info
GET https://api.spoonacular.com/recipes/findByIngredients -> Search by ingredients
GET https://api.spoonacular.com/recipes/{id}/ingredientWidget.json -> search by ingredient ID
GET https://api.spoonacular.com/recipes/{id}/nutritionWidget.json  -> Nutrition by ID
GET https://api.spoonacular.com/recipes/{id}/card -> recipe card

GET https://api.spoonacular.com/food/jokes/random -> random food joke

GET https://api.spoonacular.com/mealplanner/generate

GET https://api.spoonacular.com/mealplanner/{username}/shopping-list


Connect User
In order to call user-specific endpoints, you need to connect your app's users to spoonacular users.

Just call this endpoint with your user's information and you will get back a username and hash that you must save on your side. In future requests that you make on this user's behalf you simply pass their username and hash alongside your API key.

Read more about working with the meal planner.

POST https://api.spoonacular.com/users/connect



"""