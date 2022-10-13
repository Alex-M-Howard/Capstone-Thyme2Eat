SPOONACULAR_API_KEY = "25bf790109054f9387a17986d94ebcfb";//"1970c7ca2a3543389708d99f3a67d353";//
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


/*************************************
 * 
 * Clicking magnifying glass to expand search box
 * 
 */
$('#search-icon').on("click", () => {
  $("#search-box").animate({
    width: "toggle",
    opacity: "toggle"
  }, 450);
})


/******************************************
 * 
 *  Hide flashed messages after short delay
 * 
 */

if ($("#flashed")) {
  const timer = setTimeout(() => {
   $("#flashed").animate(
     {
       right: "-2000px",
     },
     1600
   );
    
 }, 2500)
  
  x
}