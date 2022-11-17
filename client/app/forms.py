from flask_wtf import Form
from wtforms import DateField, TextField, BooleanField, FileField, PasswordField
from wtforms.validators import *

class UserForm(Form): #defining user class
    username = TextField('username', validators=[DataRequired()]) #validates that the form isnt empty
    password = PasswordField('password', validators=[DataRequired()]) #validates that the form isnt empty

class SUForm(Form): #sign up form
    username = TextField('username', validators=[DataRequired()]) #validates that the form isnt empty
    password = PasswordField('password', validators=[DataRequired(),EqualTo('password2')]) #validates that the form isnt empty and the 2 fields match
    password2 = PasswordField('password', validators=[DataRequired()]) #validates that the form isnt empty

class BookForm(Form): #class for book forms
    title = TextField('title', validators=[DataRequired()]) #validates that the form isnt empty
    author = TextField('author', validators=[DataRequired()]) #validates that the form isnt empty
    date = DateField('date', format = '%d-%m-%Y')
    blurb = TextField('author')
    file = FileField('file')# saved to a folder
    #upvote and downvote will be implemented as thumbs up or down and default to 0 anyway
