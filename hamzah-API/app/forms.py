from flask_wtf import Form
from wtforms import DateField, TextField, BooleanField, FileField, PasswordField
from wtforms.validators import *

class League(Form): #defining user class
    league_name = TextField('league_name', validators=[DataRequired()]) #validates that the form isnt empty

