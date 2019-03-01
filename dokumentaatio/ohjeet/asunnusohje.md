Asennusohje
Git clone
Cd hakemisto
Python3 -m vena vena
source venv active
Pip install -r requirements.txt
Python3 hello.py

Lisätään heron remote gittiin
Git push Heroku master

    @staticmethod
    def work_hours_sum():
        stmt = text("SELECT accountStudent.name, hours.id FROM accountStudent"
                    " LEFT JOIN Hours ON Hours.account_id = accountStudent.id"
                    " GROUP BY accountStudent.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response