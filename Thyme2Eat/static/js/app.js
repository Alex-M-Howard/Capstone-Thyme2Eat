SPOONACULAR_API_KEY = '25bf790109054f9387a17986d94ebcfb'
BASE_RECIPES_URL = "https://api.spoonacular.com/recipes";


/*************************************
 *  
 *  Functionality for nav-bar Hamburger button
 * 
 */
$(document).ready(function () {
  // Check for click events on the navbar burger icon
  $(".navbar-burger").click(function () {
    // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
    $(".navbar-burger").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
  });
});
