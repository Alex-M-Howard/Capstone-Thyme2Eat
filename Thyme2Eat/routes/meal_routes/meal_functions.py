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
    
    new_meal = Meal(
        id=meal_id, 
        title=recipe['title'], 
        image_url=recipe['image'], 
        servings=recipe['servings'], 
        time=recipe['readyInMinutes'], 
        diets=recipe['diets'], 
        instructions = recipe['instructions'],
        meal_type=recipe['dishTypes'])
    
    db.session.add(new_meal)
    db.session.commit()

    return new_meal
