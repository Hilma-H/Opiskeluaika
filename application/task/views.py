from application import app, db
from flask import render_template, request
from application.task.models import Task

@app.route("/task/new/")
def tasks_form():
    return render_template("task/new.html")

@app.route("/task/", methods=["POST"])
def tasks_create():
    t = Task(request.form.get("name"), request.form.get("course"), request.form.get("timeHours"))

    db.session().add(t)
    db.session().commit()

    return "hello world!"