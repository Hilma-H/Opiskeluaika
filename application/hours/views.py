from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application import app, db
from application.hours.models import Hours
from application.auth.models import User
from application.hours.forms import HoursForm

@app.route("/task", methods=["GET"])
@login_required
def tasks_index():
    return render_template("task/list.html", 
    tasks = Hours.query.filter_by(account_id=current_user.id).all(), 
    list_sum = Hours.work_hours_sum(),
    under_two = Hours.under_two())

@app.route("/task/new/")
@login_required
def tasks_form():
    return render_template("task/new.html", form = HoursForm())

@app.route("/task/<hours_id>", methods=["POST"])
@login_required
def task_remove(hours_id):

    t = Hours.query.get(hours_id)
    db.session.delete(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/task/modify/<hours_id>", methods=["GET"])
@login_required
def task_modifypage(hours_id):
    return render_template("task/modify.html", form = HoursForm(), hours_id=hours_id)

@app.route("/task/modify", methods=["POST"])
@login_required
def task_modify(hours_id):
    form = HoursForm(request.form)
    task = Hours.query.get(hours_id)

    if form.course.data:
        task.course = form.course.data

    if form.time.data:
        task.timehours = form.time.data

    db.session().commit()

    return redirect(url_for("tasks_index"))

@app.route("/task/", methods=["POST"])
@login_required
def tasks_create():
    form = HoursForm(request.form)

    if not form.validate():
        return render_template("task/new.html", form = form)
    t = Hours(request.form.get("course"),
             request.form.get("time"),current_user.id)

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tasks_index"))