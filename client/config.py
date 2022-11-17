import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')#sets up path to the database
SQLALCHEMY_TRACK_MODIFICATIONS = True
WTF_CSRF_ENABLED = True #enables CSRF prevention

SECRET_KEY = 'secret-key'
