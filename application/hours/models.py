from application import db
from sqlalchemy.sql import text
from flask_login import current_user

class Hours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timehours = db.Column(db.Integer, nullable=False)
    courses_id = db.Column(db.Integer, db.ForeignKey('courses.id'),nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey('accountStudent.id'),nullable=False)
    def __init__(self, timehours, courses_id, account_id):
        self.timehours = timehours
        self.account_id = account_id
        self.courses_id = courses_id
         
    @staticmethod
    def course_hours():
        stmt = text("SELECT Courses.name, Hours.timehours, Hours.id"
        " FROM Courses, Hours"
        " WHERE Courses.id = Hours.courses_id;")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"course":row[0], "time":row[1], "id":row[2]})

        return response 


    @staticmethod
    def course_hours_for_id(id):
        stmt = text("SELECT Courses.name, Hours.timehours, Hours.id"
        " FROM Hours"
        " LEFT JOIN Courses ON Courses.id = Hours.courses_id"
        " WHERE Hours.id = :id").params(id=id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"course":row[0], "time":row[1], "id":row[2]})

        return response 


    @staticmethod
    def work_hours_sum():
        stmt = text("SELECT SUM(hours.timehours)"
        " FROM hours WHERE account_id = :id").params(id=current_user.id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"sum":row[0]})

        return response


    @staticmethod
    def hours_by_course():
        stmt = text("SELECT Courses.name, SUM(Hours.timehours)"
        " FROM Courses, Hours"
        " WHERE Courses.id=Hours.courses_id"
        " GROUP BY Courses.id")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"kurssi":row[0], "tunnit":row[1]})

        return response

    @staticmethod
    def under():
        stmt = text("SELECT Courses.name, SUM(Hours.timehours) as summa"
        " FROM Courses"
        " LEFT JOIN Hours"
        " ON Courses.id=Hours.courses_id"
        " GROUP BY Courses.id"
        " HAVING SUM(Hours.timehours)<27")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"kurssi":row[0], "tunnit":row[1]})

        return response

