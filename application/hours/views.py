from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application import app, db
from application.hours.models import Hours
from application.hours.forms import HoursForm

@app.route("/task", methods=["GET"])
@login_required
def tasks_index():
    return render_template("task/list.html", tasks = Hours.query.all())

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

@app.route("/task/<hours_id>/modify")
@login_required
def task_modify(hours_id):
    
    return redirect(url_for("task_index"))


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