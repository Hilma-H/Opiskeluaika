from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class LoginForm(FlaskForm):
    username = StringField("Käytäjätunnus")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False