from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application import app, db
from application.auth.models import User
from application.course.models import Courses
from application.course.forms import CourseForm

@app.route("/courses/", methods=["GET"])
@login_required
def courses_index():
    return render_template("course/list.html", courses = Courses.query.all())

@app.route("/courseform/")
@login_required
def courses_form():
    return render_template("course/add.html", form = CourseForm())

@app.route("/course/new", methods=["POST"])
@login_required
def course_create():
    form = CourseForm(request.form)

    if not form.validate():
        return render_template("course/add.html", form = form)

    t = Courses(request.form.get("course"))
    
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("courses_index"))

@app.route("/course/<course_id>", methods=["POST"])
@login_required
def course_remove(course_id):
    c = Courses.query.get(course_id)
    db.session.delete(c)
    db.session().commit()
  
    return redirect(url_for("courses_index"))

@app.route("/course/modifypage/<course_id>", methods=["GET","POST"])
@login_required
def course_modifypage(course_id):
    return render_template("course/modify.html", form = CourseForm(), course_id = course_id)

@app.route("/course/modify/<course_id>", methods=["POST"])
@login_required
def course_modify(course_id):
    form = CourseForm(request.form)
    course = Courses.query.get(course_id)

    if form.course.data:
        course.name = form.course.data

    db.session().commit()

    return redirect(url_for("courses_index"))

    #peruuta nappi