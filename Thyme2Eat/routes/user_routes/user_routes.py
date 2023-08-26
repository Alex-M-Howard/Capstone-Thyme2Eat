from flask import (Blueprint, flash, g, jsonify, redirect, render_template,
                   session, url_for)
from sqlalchemy.exc import IntegrityError

from ...db import db
from ...models.joke_model import Joke
from ...models.user_model import User
from ..meal_routes.meal_routes import app_meal
from .forms import LoginForm, SignupForm
from .user_functions import *

CURRENT_USER_ID = 'current_user_id'

app_user = Blueprint(
    'app_user',
    __name__,
    static_folder='../../static',
    template_folder='../../templates/user',
    url_prefix='/user'
)


# # # # # # # # # # # # # # # # # # # #
#                                     #
# User signup and login authorization #
#                                     #
# # # # # # # # # # # # # # # # # # # #

@app_user.route('/signup', methods=["GET", "POST"])
def signup_page():
    """
    Show signup form and process form submission.
    If form not valid, re-render form.
    If form valid, create new user and redirect to user dashboard.
    """
    if CURRENT_USER_ID in session:
        return redirect(url_for('app_user.home'))

    form = SignupForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
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
        flash('Welcome! Search for a meal or try our random meal generator!', "success")
        return redirect(url_for('app_user.home'))

    else:
        return render_template('/sign_up.html', form=form)


@app_user.route('/login', methods=["GET", "POST"])
def login_page():
    """
    Show login form and process form submission.
    If form not valid, re-render form.
    If form valid, log in user and redirect to user dashboard.

    """

    if CURRENT_USER_ID in session:
        return redirect(url_for('app_user.home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(
            username=form.username.data,
            password=form.password.data
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
    """
    Log out user and redirect to login page.
    """

    if CURRENT_USER_ID in session:
        del session[CURRENT_USER_ID]

    g.user = None

    flash('Successfully signed out', 'success')

    return redirect(url_for('app_user.login_page'))


def do_login(user):
    """ 
    Add user_id to session data
    """

    session[CURRENT_USER_ID] = user.id


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
    """ Show Login if not logged in, otherwise User favorites"""

    if g.user:
        return redirect(url_for('app_user.show_favorites', user_id=g.user.id))
    else:
        return redirect(url_for('app_user.login_page'))


@app_user.route('/<int:user_id>/favorites')
def show_favorites(user_id):
    """
    Show user's saved meals and random joke
    """

    user = User.query.get(g.user.id)
    joke = get_random_joke()

    return render_template('/favorites.html', user=user, joke=joke)


@app_user.route('/<int:user_id>/get_favorites')
def get_favorites(user_id):
    """ Retrieve and return saved user meals"""

    meals = retrieve_user_saved_meals(user_id)

    return jsonify(meals), 200
