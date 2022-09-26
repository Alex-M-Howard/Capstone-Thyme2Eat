from flask import Blueprint, render_template, flash, redirect, request, url_for, session, g
from sqlalchemy.exc import IntegrityError

from ...models.user_model import User
from ...models.joke_model import Joke

from .forms import SignupForm, LoginForm

from ...db import db

import random

CURRENT_USER_ID = 'current_user_id'

app_user = Blueprint(
    'app_user',
    __name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/user'
    )


@app_user.route('/')
def home():
    """ Show Logo if not logged in, otherwise User profile"""
    return render_template('/home.html')
    #return redirect(url_for('app_user.login'))

@app_user.route('/signup', methods=["GET", "POST"])
def signup():
    """ Show sign up form - Validate and create user upon success - Reject and redo on failure """

    if CURRENT_USER_ID in session:
        
        return redirect(url_for('app_user.show_profile', user_id=15))

    form = SignupForm()

    if form.validate_on_submit():
        try:
            user = User()
            form.populate_obj(user)
            
            db.session.commit()

        except IntegrityError:
            flash("Username/Email already taken", 'danger')
            print('integrity error')
            return render_template('users/signup.html', form=form)
        
        except Exception as err:
            flash("Unknown error has occurred. Try again later")
            print(err)
            return render_template('users/signup.html', form=form)

        finally:
            login(user)    
            return redirect(url_for('app_user.home'))

    else:
        return render_template('/sign_up.html', form=form)
        
        
@app_user.route('/login', methods=["GET", "POST"])
def login():
    """ Show login form """
    
    form = LoginForm()
    
    return render_template('/login.html', form=form)
    
    


@app_user.route('/<int:user_id>/profile')
def show_profile(user_id):
    print(user_id)
    return render_template('/profile.html')


#jokes = Joke.query.all()
#joke=random.choice(jokes)



# Handle logging in/out of user
@app_user.before_request
def add_user_globally():
    """If user is logged in, add user_id to Flask global"""
    
    if CURRENT_USER_ID in session:
        g.user = User.query.get(session[CURRENT_USER_ID])
    else:
        g.user = None     
        
def login(user):
    """ Log in user """
    
    session[CURRENT_USER_ID] = user.id
    
def logout():
    """ Log out current user """
    
    if CURRENT_USER_ID in session:
        del session[CURRENT_USER_ID]