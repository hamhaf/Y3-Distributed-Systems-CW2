from flask_wtf import Form
from wtforms import DateField, TextField, BooleanField, FileField, PasswordField
from wtforms.validators import *

class UserForm(Form): #defining user class
    username = TextField('username', validators=[DataRequired()]) #validates that the form isnt empty
    password = PasswordField('password', validators=[DataRequired()]) #validates that the form isnt empty