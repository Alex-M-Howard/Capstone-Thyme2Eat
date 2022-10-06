from ..db import db

from ..models.favorites_model import Favorite

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()


class User(db.Model):
    """ 
            USER MODEL
    ID           : Primary Key
    First name   : String
    Last Name    : String
    Username     : String
    Email        : String
    Password     : String -> Bcrypt to hash
    api_username : String -> To connect to Spoonacular Meal Plan
    api_password : String -> To connect to Spoonacular Meal Plan
    """
    

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    first_name = db.Column(
        db.String,
        nullable=False,
    )

    last_name = db.Column(
        db.String,
        nullable=False
    )

    username = db.Column(
        db.String,
        nullable=False,
        unique=True,
    )

    email = db.Column(
        db.String,
        nullable=False,
        unique=True,
    )

    password = db.Column(
        db.String,
        nullable=False,
    )
    
    api_username = db.Column(
        db.String,
        nullable=True,
    )
    
    api_password = db.Column(
        db.String,
        nullable=True,
    )
    
    
    
    favorites = db.relationship('Meal', 
                                secondary='favorites',
                                primaryjoin=(Favorite.user_id==id),
                                )
    
    def __repr__(self):
        return f"<User #{self.id}: {self.first_name} {self.last_name} -> {self.username}, {self.email}>"


    @classmethod
    def signup(cls, first_name, last_name, username, email, password):
        """
          Hash password using Bcrypt
          Create New User
          Add to DB
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            first_name=first_name,
            last_name=last_name,
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
