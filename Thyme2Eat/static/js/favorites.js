
/*************************************
 *
 *  Add event listener for meal type tabs
 *  Prevent Default Button Function
 *  Call getFavorites function
 * 
 */
$("#favorite-tabs").on("click", "a", async (event) => {
  event.preventDefault();

  // Remove random joke from page
  $("#joke").remove();
  getFavorites(event);
});


/*************************************
 * 
 * @param {object - HTML element} event
 * @param {String - Selected Meal Filter from REMOVE BUTTON} mealType 
 * Clear previous results
 * Set tab to active
 * Get user favorites in that category
 * Call showFavoriteMeal
 * 
 */
const getFavorites = async (event, mealType) => {
  $("#results").empty();

  if(event){
    // Selecting Filter Tabs
    $("ul").children("li").removeClass("is-active");
    $(event.target).closest("li").toggleClass("is-active");
    mealType = $(event.target).closest("li").attr("id");
  }

  let meals = await getUserFavorites();

  showFavoriteMeal(meals, mealType);
  checkIfNoMeals(); ////////////////////////////////////////////////////////////////////////////////////////////ADDDDDDDD
  addRemoveListener(mealType);
};


/*************************************
 * 
 * @param {Array - User Favorites} meals 
 * @param {String - Selected Meal Filter} mealType 
 * Create Meal Cards and append to #results
 * 
 */
const showFavoriteMeal = (meals, mealType) => {
  for (let meal of meals) {
    
    if (meal.meal_type.includes(mealType)) {
      let div = $("<div>").addClass(
        "column is-one-quarter-desktop is-one-quarter-widescreen is-one-third-tablet"
      ).html(`
          <div class="card">
            <div class="card-image">
                <figure class="image is-4by3">
                  <a href="/meals/recipe/${meal.id}">  
                  <img src="${meal.image}" alt="${meal.title} image">
                  </a>
                </figure>
            </div>

            <div class="card-header">
              <div class="card-header-title">
                <a href="/meals/recipe/${meal.id}"><p style="font-size: 1rem;">${meal.title}</p></a>
              </div>
            </div>
        `);

      $("#results").append($(div));

      $("div.card-header-title:last").html(
        $("div.card-header-title:last").html() +
        `<a id="remove-button" class="buttons is-align-content-flex-end"><i class="fa-solid fa-heart" data-meal_id=${meal.id}></i><a>`
      );
    }
  }
};


/*************************************
 * 
 * @returns Array - User Favorited Meals
 * 
 */
const getUserFavorites = async () => {
  const responsePromise = await axios.get(`/user/${userId}/get_favorites`);

  return responsePromise.data;
};



/*************************************
 *
 *  Add event listener for removing meal
 *  Prevent Default Button function
 *  Call removeSavedRecipe function
 *  Call getFavorites function
 * 
 */
const addRemoveListener = (mealType) => {
$(".buttons").on("click", async (event) => {
  event.preventDefault();

  let mealId = $(event.target).data("meal_id");
  
  removeSavedRecipe(mealId);
  $(event.target).closest('.column').remove();
  checkIfNoMeals();
});  
}

/**
 * 
 * Remove a favorite from User's Profile
 * 
 */
const removeSavedRecipe = async (mealId) => {
  const responsePromise = axios.delete(`/meals/${mealId}/remove`)

}

const checkIfNoMeals = () => {
  if (!$("#results").html()) {
    $("#results")
      .html(`
    <div class="column is-4"></div>
    <div class="column is-4 has-text-centered">No meals found</div>
    <div class="column is-4"></div>
    `
      )
  }
}