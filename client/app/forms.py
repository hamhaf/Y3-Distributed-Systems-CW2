from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import *

class CountryForm(Form): #defining user class
    country = TextField('country')