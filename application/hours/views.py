from application import app, db
from flask import render_template, request, redirect, url_for
from application.hours.models import Hours
from application.hours.forms import HoursForm

@app.route("/task", methods=["GET"])
def tasks_index():
    return render_template("task/list.html", tasks = Hours.query.all())

@app.route("/task/new/")
def tasks_form():
    return render_template("task/new.html", form = HoursForm())

@app.route("/task/", methods=["POST"])
def tasks_create():
    form = HoursForm(request.form)

    if not form.validate():
        return render_template("task/new.html", form = form)
    t = Hours(request.form.get("name"),
             request.form.get("course"),
             request.form.get("time"))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tasks_index"))