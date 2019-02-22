from application import db
from sqlalchemy.sql import text
from flask_login import current_user

class Hours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(144), nullable=False)
    timeHours = db.Column(db.Integer, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('accountStudent.id'),nullable=False)
    def __init__(self, course, timeHours, account_id):
        self.course = course
        self.timeHours = timeHours
        self.account_id = account_id

    @staticmethod
    def work_hours_sum():
        stmt = text("SELECT SUM(hours.timehours) FROM hours WHERE account_id =" + str(current_user.id))

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"sum":row[0]})

        return response

    @staticmethod
    def under_two():
        stmt = text("SELECT COUNT(hours.timehours) FROM hours WHERE timeHours<2")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"under":row[0]})

        return response