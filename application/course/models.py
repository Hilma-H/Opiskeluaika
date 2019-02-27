from application import db
from sqlalchemy.sql import text
from flask_login import current_user

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    hours = db.relationship("Hours", backref='courses', lazy=True)
    def __init__(self, name):
        self.name = name