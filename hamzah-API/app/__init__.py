from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from logging import *

FORMAT = '%(asctime)s : %(message)s'
basicConfig(filename='info.log',level=DEBUG)

app = Flask(__name__) #creates flask object
app.config.from_object('config') #applies configurations made in config file to object
db = SQLAlchemy(app)

migrate = Migrate(app, db, render_as_batch=True)

admin = Admin(app,template_mode='bootstrap3')

log = getLogger('werkzeug')
log.setLevel(ERROR)

from app import views
from app import models
