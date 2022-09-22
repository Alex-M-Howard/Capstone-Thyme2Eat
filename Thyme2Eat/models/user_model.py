""" 
        USER MODEL
  ID         : Primary Key
  Username   : Text
  Email      : Text
  Password   : Text -> Bcrypt to hash
"""

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

#TODO MOVE THESE TO ANOTHER FILE
bcrypt = Bcrypt()
db = SQLAlchemy()   

class User(db.Model):
    """User in the system."""

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    username = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    email = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    password = db.Column(
        db.Text,
        nullable=False,
    )

    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"


    @classmethod
    def signup(cls, username, email, password):
        """
          Hash password using Bcrypt
          Create New User
          Add to DB
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            email=email,
            password=hashed_pwd
        )

        db.session.add(user)
        return user


    @classmethod
    def authenticate(cls, username, password):
        """
        Find user with provided username and password
        
        If found -> return user
        Else     -> return False
        """

        user = cls.query.filter_by(username=username).first()

        if user:
            is_authorized = bcrypt.check_password_hash(user.password, password)
            if is_authorized:
                return user

        return False
