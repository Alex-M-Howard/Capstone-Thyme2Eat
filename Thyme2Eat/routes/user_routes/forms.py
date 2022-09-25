from flask_wtf import FlaskForm

from wtforms_alchemy import ModelForm, model_form_factory

from wtforms.validators import Email, DataRequired, Length
from wtforms.fields import PasswordField
from ...models.user_model import User

from ...db import db

# NEEDED TO MAKE WTFORMS ALCHEMY WORK WITH FLASK WTFORMS
BaseModelForm = model_form_factory(FlaskForm)

class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session

class SignupForm(ModelForm):
    """Form for a user to sign-up"""

    class Meta:
        model = User
        password = PasswordField()
        
        validators = {'username': [DataRequired(), Length(min=6)],
                      'email': [DataRequired(),Email()],
                      'password': [DataRequired()]
                      }

class LoginForm(ModelForm):
    """Form for user to login"""
    
    class Meta:
        model = User
        only=['username', 'password']
        password = PasswordField()
        
        validators = {'username': [DataRequired(), Length(min=6)],
                      'password': [DataRequired()]
                      }
