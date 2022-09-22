from flask import Blueprint, render_template, flash, redirect, request

routes = Blueprint(
    'routes',
    __name__,
    static_folder='static',
    template_folder='templates'
    )

@routes.route('/')
def home():
    return render_template('/testing/test.html')
