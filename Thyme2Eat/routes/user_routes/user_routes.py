from flask import Blueprint, render_template, flash, redirect, request
# Use url_for for redirects, render_templates otherwise

app_user = Blueprint(
    'app_user',
    __name__,
    static_folder='static',
    template_folder='templates'
    )

@app_user.route('/')
def home():
    return render_template('/home.html')
