from flask import Blueprint, render_template, flash, redirect, request

from ...models.joke_model import Joke

import random

app_user = Blueprint(
    'app_user',
    __name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/user'
    )

@app_user.route('/')
def home():
    
    jokes = Joke.query.all()
    
    return render_template('/home.html', joke=random.choice(jokes))
