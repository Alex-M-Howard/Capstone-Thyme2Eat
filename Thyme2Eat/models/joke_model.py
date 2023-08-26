from ..db import db


class Joke(db.Model):
    """ 
            Joke MODEL
    ID         : Primary Key
    Text      : Text
    """
    __tablename__ = 'jokes'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Joke #{self.id}: {self.text}>"
