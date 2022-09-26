from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField
from wtforms.validators import Email, InputRequired, Length


class SignupForm(FlaskForm):
    """Form for a user to sign-up"""

    username = StringField("Username", validators=[InputRequired(message='You must enter a username'), Length(min=6)])
    email = StringField("Email", validators=[InputRequired(), Email(granular_message=True)])
    password = PasswordField("Password", validators=[InputRequired(message='You must enter a password')])
    

class LoginForm(FlaskForm):
    """Form for user to login"""
    
    username = StringField("Username", validators=[InputRequired(message='You must enter a username')])
    password = PasswordField("Password", validators=[InputRequired(message='You must enter a password')])

