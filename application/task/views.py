from application import app
from flask import render_template, request

@app.route("/task/new/")
def tasks_form():
    return render_template("task/new.html")

@app.route("/task/", methods=["POST"])
def tasks_create():
    print(request.form.get("name"))
  
    return "hello world!"