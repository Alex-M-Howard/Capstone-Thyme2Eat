SPOONACULAR_API_KEY = '25bf790109054f9387a17986d94ebcfb'
BASE_RECIPES_URL = "https://api.spoonacular.com/recipes";

NUMBER_OF_RESULTS = 24



/*************************************
 * 
 *  Add event listener for search button
 *  Prevent Default Button Function
 *  Get random meals
 *  Show meals on page
 * 
 */

$('#random-meal-search').on('click', (async (event) => {
    event.preventDefault()

    let meals = await getRandomMeals();
    showMeals(meals);
}))


/*************************************
 * 
 *  getRandomMeals
 *  Axios.get API Request for Random Meals
 *  Returns an array of objects
 * 
 */

const getRandomMeals = async () => {
    let diet = $("#diet").val();
    let type = $("#type").val();
    let intolerances = $("#intolerances").val();
    let apiKey = SPOONACULAR_API_KEY;
    let number = NUMBER_OF_RESULTS;
    let sort = "random";
    let instructionsRequired = "true";

    let params = {
        apiKey,
        diet,
        intolerances,
        type,
        number,
        sort,
        instructionsRequired,
    }; 

    const response = await axios.get(`${BASE_RECIPES_URL}/complexSearch`, {params});

    return response.data.results;
} 


/*************************************
 * 
 *  showMeals
 *  Loop through meals
 *  Add card divs to create meal cards
 *  Display on page
 * 
 */

const showMeals = (meals) => {
    
    for (meal of meals) {
        $("#results").append(
            $("<div>")
            .addClass("column is-one-quarter-desktop is-one-quarter-widescreen is-one-third-tablet")
            .html(`
          <div class="card">
            <div class="card-image">
              
                <figure class="image is-4by3">
                <a href="{{ url_for('app_meal.show_recipe', meal_id=${meal.id}) }}">  
                <img src="${meal.image}" alt="${meal.title} image">
                </figure>
              </a>
            </div>

            <div class="card-header">
              <div class="card-header-title">
                <a href="{{ url_for('app_meal.show_recipe', meal_id=${meal.id}) }}"><p style="font-size: 1rem;">${meal.title}</p></a>
                
                {% if g.user %}
                <form action='{{ url_for("app_user.save_recipe", user_id=g.user.id) }}'method="POST">
                  <button class="button is-primary" type="submit">Save Recipe</button>
                </form>
                {% endif %}
              
              </div>
            </div>
        `
            )
        ) 
    }
}