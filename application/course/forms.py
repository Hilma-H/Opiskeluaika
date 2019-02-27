from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CourseForm(FlaskForm):
    course = StringField("Kurssi: ", [validators.Length(min=2, max=140)])
    class Meta:
        csrf = False