// Add event listener for meal type tabs
// When a tab is clicked, prevent the default action, remove any random joke from the page, and fetch user's favorite meals
$("#favorite-tabs").on("click", "a", async (event) => {
  event.preventDefault();

  // Remove any random joke from the page
  $("#joke").remove();
  
  // Fetch user's favorite meals based on the selected tab and display them
  getFavorites(event);
});


/*************************************
 * Fetch and Display User's Favorite Meals
 * 
 * @param {object - HTML element} event - The click event triggered by the tab selection
 * @param {String - Selected Meal Filter from tab} mealType - The type of meal selected from the tab
 * 
 * Steps:
 * - Clear the previous results
 * - Highlight the active tab and determine the meal type
 * - Fetch user's favorite meals
 * - Display the favorite meals based on the meal type
 * - Add listener for removing meals
 * 
 */
const getFavorites = async (event, mealType) => {
  // Clear previous results
  $("#results").empty();

  // Highlight the active tab and determine the meal type
  if (event) {
    $("ul").children("li").removeClass("is-active");
    $(event.target).closest("li").toggleClass("is-active");
    mealType = $(event.target).closest("li").attr("id");
  }

  // Fetch user's favorite meals
  let meals = await getUserFavorites();

  // Display favorite meals based on the selected meal type
  showFavoriteMeal(meals, mealType);
  
  // Check if there are no meals and notify the user
  checkIfNoMeals();
  
  // Add listener for removing meals from the favorites
  addRemoveListener(mealType);
};


/*************************************
 * Display User's Favorite Meals
 * 
 * @param {Array - User Favorites} meals - List of user's favorite meals
 * @param {String - Selected Meal Filter} mealType - The type of meal selected
 * 
 * Steps:
 * - Iterate through each favorite meal
 * - Check if the meal matches the selected meal type or is uncategorized
 * - Create a card for the meal and append it to the results section
 * 
 */
const showFavoriteMeal = (meals, mealType) => {
  for (let meal of meals) {
    if (
      meal.meal_type.includes(mealType) ||
      (mealType === "Uncategorized" &&
        !meal.meal_type.includes('snack') &&
        !meal.meal_type.includes('breakfast') &&
        !meal.meal_type.includes('lunch') &&
        !meal.meal_type.includes('side'))
    ) {
      // Create a meal card and append it to the results section
      let div = $("<div>").addClass(
        "column is-one-quarter-desktop is-one-quarter-widescreen is-one-third-tablet"
      ).html(`
          <div class="card">
            <!-- Card image -->
            <div class="card-image">
              <figure class="image is-4by3">
                <a href="/meals/recipe/${meal.id}">  
                  <img src="${meal.image}" alt="${meal.title} image">
                </a>
              </figure>
            </div>

            <!-- Card header -->
            <div class="card-header">
              <div class="card-header-title">
                <a href="/meals/recipe/${meal.id}"><p style="font-size: 1rem;">${meal.title}</p></a>
              </div>
            </div>
        `);

      // Append the card to the results section
      $("#results").append($(div));

      // Add a remove button to the card header
      $("div.card-header-title:last").html(
        $("div.card-header-title:last").html() +
        `<a id="remove-button" class="buttons is-align-content-flex-end"><i class="fa-solid fa-heart" data-meal_id=${meal.id}></i><a>`
      );
    }
  }
};


/*************************************
 * Fetch User's Favorite Meals from Server
 * 
 * @returns Array - List of User's Favorited Meals
 * 
 */
const getUserFavorites = async () => {
  const responsePromise = await axios.get(`/user/${userId}/get_favorites`);
  return responsePromise.data;
};


/*************************************
 * Add Event Listener for Removing Meals
 * 
 * @param {String - Selected Meal Filter} mealType - The type of meal selected
 * 
 * Steps:
 * - Add click event listener for the remove button
 * - Prevent the default button action
 * - Delete the meal from the user's favorites
 * - Remove the meal card from the page
 * 
 */
let inProgress = false;

const addRemoveListener = (mealType) => {
  $(".buttons").on("click", async (event) => {
    event.preventDefault();

    // Prevent multiple removal requests while processing
    if (inProgress) {
      return;
    }

    // Get the meal ID from the clicked button
    let mealId = $(event.target).data("meal_id");
    
    // Send a request to remove the meal
    const responsePromise = axios.delete(`/meals/${mealId}/remove`);

    // Handle the response
    responsePromise
      .then(
        (onFulfilled) => {
          // Remove the meal card from the page
          $(event.target).closest(".column").remove();
          checkIfNoMeals();
        },
        (onFailure) => {
          // Display an error message briefly
          $("error").toggleClass("is-active");
          const timer = setTimeout(() => {
            $("error").toggleClass("is-active");
          }, 1500);
        }
      )
      .finally(() => {
        inProgress = false;
      });
  });
};

/*************************************
 * Check If No Meals and Notify User
 * 
 */
const checkIfNoMeals = () => {
  if (!$("#results").html()) {
    // Display a message if no meals are found
    $("#results")
      .html(`
    <div class="column is-4"></div>
    <div class="column is-4 has-text-centered">No meals found</div>
    <div class="column is-4"></div>
    `);
  }
};
