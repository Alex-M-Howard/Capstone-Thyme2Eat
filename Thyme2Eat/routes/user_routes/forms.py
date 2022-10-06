from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField
from wtforms.validators import Email, InputRequired, Length


class SignupForm(FlaskForm):
    """Form for a user to sign-up"""

    first_name = StringField("First Name", validators=[InputRequired(message='You must enter a first name'), Length(max=35)])
    last_name = StringField("Last Name", validators=[InputRequired(message='You must enter a last name'), Length(max=35)])
    username = StringField("Username", validators=[InputRequired(message='You must enter a username'), Length(min=6, max=20)])
    email = StringField("Email", validators=[InputRequired(), Email(granular_message=True)])
    password = PasswordField("Password", validators=[InputRequired(message='You must enter a password'), Length(min=6)])
    

class LoginForm(FlaskForm):
    """Form for user to login"""
    
    username = StringField("Username", validators=[InputRequired(message='You must enter a username')])
    password = PasswordField("Password", validators=[InputRequired(message='You must enter a password'), Length(min=6, message="Password must be at least 6 characters in length")])

