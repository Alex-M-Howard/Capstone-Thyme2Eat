from flask import Blueprint, render_template, flash, redirect, url_for, session, g, jsonify
from sqlalchemy.exc import IntegrityError

from ...models.user_model import User
from ...models.joke_model import Joke

from ...db import db

from ..meal_routes.meal_routes import app_meal

from .user_functions import *

from .forms import SignupForm, LoginForm




CURRENT_USER_ID = 'current_user_id'

app_user = Blueprint(
    'app_user',
    __name__,
    static_folder='../../static',
    template_folder='templates',
    url_prefix='/user'
    )


# # # # # # # # # # # # # # # # # # # #
#                                     #
# User signup and login authorization #
#                                     #
# # # # # # # # # # # # # # # # # # # #

@app_user.route('/signup', methods=["GET", "POST"])
def signup_page():
    """ Show sign up form - Validate and create user upon success - Reject and redo on failure """

    if CURRENT_USER_ID in session:
        return redirect(url_for('app_user.show_profile', user_id=session[CURRENT_USER_ID]))

    form = SignupForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                username=form.username.data,
                password=form.password.data,
                email=form.email.data
            )

            db.session.commit()
    
        except IntegrityError:
            flash("Username/Email already taken", 'danger')
            return render_template('/sign_up.html', form=form)
        
        except Exception as err:
            flash("Unknown error has occurred. Try again later")
            print(err)
            return render_template('/sign_up.html', form=form)

        do_login(user)    
        return redirect(url_for('app_user.home'))

    else:
        return render_template('/sign_up.html', form=form)

@app_user.route('/login', methods=["GET", "POST"])
def login_page():
    """ Show login form """

    if CURRENT_USER_ID in session:
        return redirect(url_for('app_user.show_profile', user_id=session[CURRENT_USER_ID]))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.authenticate(
            username = form.username.data,
            password = form.password.data
        )
            
        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect(url_for('app_user.home'))
        else:
            flash("Invalid Credentials.", "danger")
            
    return render_template('/login.html', form=form)

@app_user.route('/logout', methods=["GET"])
def logout_user():
    """Initiate Logout"""
    
    do_logout()
    flash('Successfully signed out', 'success')
    
    return redirect(url_for('app_user.login_page'))

def do_login(user):
    """ Log in user """
    
    session[CURRENT_USER_ID] = user.id
    
def do_logout():
    """ Log out current user """
    
    if CURRENT_USER_ID in session:
        del session[CURRENT_USER_ID]

# Give user object to user & meal routes
@app_user.before_request
@app_meal.before_request
def add_user_globally():
    """If user is logged in, add user_id to Flask global for app_meal and app_user"""
    
    if CURRENT_USER_ID in session:
        g.user = User.query.get(session[CURRENT_USER_ID])
    else:
        g.user = None
        


# # # # # # # # # # # # # # # # # # # #
#                                     #
#   Dashboard, Favorites, Meal Plan   #
#                                     #
# # # # # # # # # # # # # # # # # # # #

@app_user.route('/')
def home():
    """ Show Logo if not logged in, otherwise User profile"""
    return render_template('/home.html')   
               
@app_user.route('/<int:user_id>/profile')
def show_profile(user_id):
    
    return render_template('/profile.html')
               
@app_user.route('/<int:user_id>/favorites')
def show_favorites(user_id):
    
    user = User.query.get(g.user.id)
    joke = get_random_joke()
    
    return render_template('/favorites.html', user=user, joke=joke)

@app_user.route('/<int:user_id>/get_favorites')
def get_favorites(user_id):
    """ Retrieve and return saved user meals"""
    
    meals = retrieve_user_saved_meals(user_id)
        
    return jsonify(meals), 200

@app_user.route('/<int:user_id>/remove_favorite/<int:meal_id>', methods=['DELETE'])
def remove_from_favorites(user_id, meal_id):
    """Remove a recipe from user's DB"""
    
    remove_saved_recipe(user_id, meal_id)
    
    return jsonify({'result': 'deleted'}), 200
    