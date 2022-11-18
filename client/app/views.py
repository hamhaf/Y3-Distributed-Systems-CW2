from flask import render_template, flash, request, redirect, url_for, g, session
from app import app
from .forms import CountryForm
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import exists
import os,time
from datetime import date
from werkzeug.utils import secure_filename
import requests

@app.route('/')
def index():#the home page will be the login/sign up page
	form = CountryForm()
	return render_template('home.html', title='Country Select', form=form)#renders the home.html template passing the appropriate variabels

@app.route('/findLeague', methods=['GET'])
def findLeague():
    form = CountryForm()
    country = form.country.data
    league = requests.get(f"127.0.0.1:8001/league/getleague/{country}")
    print(league)
    return redirect(url_for())

@app.route('showLeague')
def showLeague():
    # teams = list of teams from adams api
    return render_template('showLeague.html', title='League Name'```, teams = teams```)