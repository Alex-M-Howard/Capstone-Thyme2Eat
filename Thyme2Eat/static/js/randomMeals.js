NUMBER_OF_RANDOM_RESULTS = 12;

/*************************************
 *
 *  Add event listener for search button
 *  Prevent Default Button Function
 *  Get random meals
 *  Show meals on page
 *  Add Event Listeners to SAVE buttons
 *
 */
$("#random-meal-search").on("click", async (event) => {
  event.preventDefault();

  let meals = await getRandomMeals();
  $("#results").empty();
  showMeals(meals);
  saveRecipeEvent();
});

/*************************************
 *
 *  getRandomMeals
 *  Axios.get API Request for Random Meals   --> /complexSearch
 *  Returns an array of objects
 *
 */
const getRandomMeals = async () => {
  let diet = $("#diet").val();
  let type = $("#type").val();
  let intolerances = $("#intolerances").val();
  let apiKey = SPOONACULAR_API_KEY;
  let number = NUMBER_OF_RANDOM_RESULTS;
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

  const response = await axios.get(`${BASE_RECIPES_URL}/complexSearch`, {
    params,
  });

  return response.data.results;
};

/*************************************
 *
 *  showMeals
 *  Loop through meals
 *  Create meal cards
 *  Display on page
 *  If user is logged in, create SAVE button
 *
 */
const showMeals = (meals) => {
  for (let meal of meals) {
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
                <div class="columns">
                  <div class="column is-three-quarters">
                    <a href="/meals/recipe/${meal.id}"><p style="font-size: 1rem;">${meal.title}</p></a>
                  </div>
                  <div class="column is-one-quarter button-location"></div>
                </div>
              </div>
            </div>
        `);

    $("#results").append($(div));

    // If user logged in, create SAVE buttons
    if (user !== "None") {
      // If meal already in user favorites, Have Remove button instead
      if (user_meals.includes(meal.id)) {
        $("div.button-location:last").html(
          $("div.button-location:last").html() +
            `<a id="remove-button" class="buttons is-align-content-flex-end"><i class="fa-solid fa-heart" data-meal_id=${meal.id}></i><a>`
        );
      } else {
        $("div.button-location:last").html(
          $("div.button-location:last").html() +
            `<a id="save-button" class="buttons is-align-content-flex-end"><i class="fa-regular fa-heart" data-meal_id=${meal.id}></i><a>`
        );
      }
    }
  }
};

/*************************************
 *
 *  Add event listener for SAVE buttons
 *  Prevent Default Button Function
 *  Call USER route to Save/Remove Meal
 *
 */
const saveRecipeEvent = () => {
  $(".buttons").on("click", async (event) => {
    event.preventDefault();

    let mealId = $(event.target).data("meal_id");

    const responsePromise = axios.post(`/meals/${mealId}/save`);
    changeButton($(event.target));

  });
};

/*************************************
 *
 *  Change button text on randomly
 *  generated meals.
 *  Save --> Remove
 *  Remove --> Save
 */
const changeButton = (button) => {
    $(button).toggleClass("fa-solid fa-heart");
    $(button).toggleClass("fa-regular fa-heart");    
};
