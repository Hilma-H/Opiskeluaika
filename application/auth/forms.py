from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käytäjätunnus")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Nimi: ", [validators.Length(min=2, max=140)])
    username = StringField("Käyttäjätunnus: ", [validators.Length(min=2, max=140)])
    password = StringField("Salasana", [validators.Length(min=2, max=140)])
 
    class Meta:
        csrf = False