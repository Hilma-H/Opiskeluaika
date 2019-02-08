from application import db

class Hours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(144), nullable=False)
    timeHours = db.Column(db.Integer, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('accountStudent.id'),nullable=False)
    def __init__(self, course, timeHours, account_id):
        self.course = course
        self.timeHours = timeHours
        self.account_id = account_id