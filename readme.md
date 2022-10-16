# Capstone 1 - Thyme2Eat
Skip right to the project --> [Thyme2Eat](https://thyme2eat.up.railway.app)
<hr>

#### Tech Used
**Database**
* [PostgreSQL](https://www.postgresql.org/)
<br>

**Front End (HTML, CSS, JS)**
* [jQuery](https://api.jquery.com/)
* [Axios](https://axios-http.com/)
* [Bulma](https://bulma.io) 
* [FontAwesome](https://fontawesome.com/)

<br>

**Back End (Python)**
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [SQL-Alchemy](https://flask-sqlalchemy.palletsprojects.com/)
* [WTForms](https://wtforms.readthedocs.io/en/3.0.x/)
* [Bcrypt](https://github.com/pyca/bcrypt/)

<hr>

#### Installing Project
1. Clone Repository
2. Create Virtual Environment
3. Install Requirements
4. Create/Seed Database
5. Run Flask

<br>
##### --- Clone Repository ---
Clone repository to your workspace:

`git clone https://github.com/Alex-M-Howard/Capstone-Thyme2Eat.git`
`cd Capstone-Thyme2Eat`

<br>

##### --- Create Virtual Environment ---
Create virtual environment:

`python -m venv venv`
<br>

##### --- Install Requirements ---
Activate you virtual environment and then use pip to install required pacakges:

`pip install -r requirements.txt`
<br>

##### --- Seed Database | PostgreSQL ---
Seed database:

`psql < seed.SQL'

<br>

##### --- Run Flask ---
Next, start the Flask server:

`flask ---app Thyme2Eat run`

Now in your broswer, navigate to your local host to see the app!

<hr>

#### Routes 
##### Sign Up
If it is your first time here, click on Sign Up and create an account, otherwise login! You can also view randomly generated meals without being logged in, just use the navbar.
<br>

##### Get Random Meals
Using the filters of your choice, get random meals that you can view. Click on their picture or title to see the full recipe. If you're logged in, you can click the heart icon to save the recipe to "Your Recipes" and view them anytime you want. 
<br>

##### My Recipes
When logged in, you will be directed to your saved meals which can be filtered by: Breakfast|Brunch, Snacks, Sides, Lunch|Dinner, and Uncategorized. To remove a recipe, click on the heart icon.
<br>

##### Search Recipes
If you have an idea what you want to find, click on the magnifying glass on the navbar and search for a meal!
<br>

##### Viewing Recipe
You can see the servings, time to cook, ingredients list, instructions, and also the nutrition facts. If you'd like to print this to keep in your own cookbook, click the printer icon to be directed to a printable page of your chosen recipe! If this recipe is not quite cutting it, there might be a similar recipe that has just the tweak it needs at the bottom of the page!

