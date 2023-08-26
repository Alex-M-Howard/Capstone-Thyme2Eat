// Add event listener for search button
// When the button is clicked, prevent default action, fetch random meals, display them, and set up save button events
$("#random-meal-search").on("click", async (event) => {
  event.preventDefault();

  // Fetch random meals
  let meals = await getRandomMeals();
  
  // Clear previous results and display fetched meals
  $("#results").empty();
  showMeals(meals);
  
  // Set up event listeners for saving/removing recipes
  saveRecipeEvent();
});

/*************************************
 * Fetch Random Meals
 * 
 * @returns Array - List of Random Meal Objects
 * 
 * Steps:
 * - Get diet, type, and intolerances parameters from the form
 * - Send a request to fetch random meals with the specified parameters
 * - Return an array of meal objects
 * 
 */
const getRandomMeals = async () => {
  let diet = $("#diet").val();
  let type = $("#type").val();
  let intolerances = $("#intolerances").val();

  let params = {
    diet,
    intolerances,
    type,
  };

  const response = await axios.get(`/meals/random/recipes`, {
    params,
  });

  return response.data.results;
};

/*************************************
 * Display Meals on Page
 * 
 * @param {Array - Meal Objects} meals - List of meal objects to be displayed
 * 
 * Steps:
 * - Iterate through each meal
 * - Create a meal card and append it to the results section
 * - If the user is logged in, add appropriate save/remove button
 * 
 */
const showMeals = (meals) => {
  for (let meal of meals) {
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
                <div class="columns">
                  <div class="column is-three-quarters">
                    <a href="/meals/recipe/${meal.id}"><p style="font-size: 1rem;">${meal.title}</p></a>
                  </div>
                  <div class="column is-one-quarter button-location"></div>
                </div>
              </div>
            </div>
        `);

    // Append the card to the results section
    $("#results").append($(div));

    // If user is logged in, add appropriate save/remove button
    if (user !== "None") {
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
 * Save/Remove Button Event Listener
 * 
 * Steps:
 * - Add click event listener for the save/remove button
 * - Prevent the default button action
 * - Identify if the target is an anchor tag and adjust accordingly
 * - Determine the meal ID
 * - If the button is already active, remove the meal, otherwise save it
 * 
 */
let inProgress = false;

const saveRecipeEvent = () => {
  $(".buttons").on("click", async (event) => {
    console.log('clicked');
    event.preventDefault();

    if (inProgress) {
      return;
    }

    // Adjust the event target if an anchor tag was clicked
    if ($(event.target).is("a")) {
      event.target = $(event.target).children("i");
    }

    // Determine the meal ID
    let mealId = $(event.target).data("meal_id");

    // Handle saving or removing the meal
    if ($(event.target).hasClass("fa-solid")) {
      inProgress = true;
      const responsePromise = axios.delete(`/meals/${mealId}/remove`);
      responsePromise
        .then(
          (onFulfilled) => {
            changeButton($(event.target));
          },
          (onFailure) => {
            $("error").toggleClass("is-active")
            const timer = setTimeout(() => {
              $("error").toggleClass("is-active");
            }, 1500)
          })
        .finally(() => {
            inProgress = false;
        })
      
    } else {
      inProgress = true;
      const responsePromise = axios.post(`/meals/${mealId}/save`);
      responsePromise
        .then(
          (onFulfilled) => {
            changeButton($(event.target));
          },
          (onFailure) => {
            $("error").toggleClass("is-active");
            const timer = setTimeout(() => {
              $("error").toggleClass("is-active");
            }, 1500);
          }
        )
        .finally(() => {
          inProgress = false;
        });
    }
  });
};

/*************************************
 * Toggle Save/Remove Button
 * 
 * @param {jQuery object} button - The clicked button element
 * 
 * Steps:
 * - Toggle between solid and regular heart icons
 * 
 */
const changeButton = (button) => {
    $(button).toggleClass("fa-solid fa-heart");
    $(button).toggleClass("fa-regular fa-heart");    
};

// Set up event listeners for show_recipe to favorite/unfavorite meals
saveRecipeEvent();
