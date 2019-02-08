from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class HoursForm(FlaskForm):
    course = StringField("Kurssi: ", [validators.InputRequired(message='Kenttä ei voi olla tyhjä')])
    time = StringField("Käytetty aika (tunteina): ")
 #, [validators.NumberRange(min=0, max=999, message=None)]
    class Meta:
        csrf = False