# Flask-login määrää, että jokaisella käyttäjälle on
# metodit get_id, is_active, is_anonymous sekä is_authenticated

from application import db
from sqlalchemy.sql import text

class User(db.Model):

    __tablename__ = "accountStudent"
  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    hours = db.relationship("Hours", backref='accountStudent', lazy=True)
  

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
