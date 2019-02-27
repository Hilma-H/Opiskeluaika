from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, validators

class HoursForm(FlaskForm):
    time = IntegerField("Käytetty aika (tunteina): ", [validators.NumberRange(min=0, max=999, message=None)])

    class Meta:
        csrf = False

  