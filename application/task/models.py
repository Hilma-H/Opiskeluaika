from application import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    course = db.Column(db.String(144), nullable=False)
    timeHours = db.Column(db.Integer, nullable=False)

    def __init__(self, name, course, timeHours):
        self.name = name
        self.course = course
        self.timeHours = timeHours