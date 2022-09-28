from flask import Blueprint, render_template, flash, redirect, request, url_for, g

from ...models.meal_model import Meal

from .meal_functions import get_recipe, get_nutrition


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
    
    recipe = get_recipe(meal_id)
    nutrition = get_nutrition(meal_id)

    return render_template('show_recipe.html', recipe=recipe, nutrition=nutrition)
    
@app_meal.route('/<int:meal_id>/save', methods=["POST"])
def save_recipe(meal_id):
    """ Save recipe to User's recipe book"""
    
    
    recipe = get_recipe(meal_id)
    
    
    # TODO --> Check if meal in database, or add meal
    new_meal = Meal(
        id=meal_id, 
        title=recipe.title, 
        image_url=recipe.image, 
        servings=recipe.servings, 
        time=recipe.readyInMinutes, 
        diets=recipe.diets, 
        instructions = recipe.analyzedInstructions,
        meal_type=recipe.dishTypes)
    
    db.session.add(new_meal)
    db.session.commit()
    
    return new_meal

