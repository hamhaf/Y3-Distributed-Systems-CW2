from flask import render_template, flash, request, redirect, url_for, g, session
from app import app
from .forms import CountryForm
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import exists
import os,time
from datetime import date
from werkzeug.utils import secure_filename
import requests
import http.client


@app.route('/')
def index():#the home page will be the login/sign up page
	form = CountryForm()
	return render_template('home.html', title='Country Select', form=form)#renders the home.html template passing the appropriate variabels

@app.route('/findLeague', methods=['POST','GET'])
def findLeague():
    form = CountryForm()
    country = form.country.data
    try:
        conn = http.client.HTTPSConnection("127.0.0.1:8001")
        conn.request("GET",f"/league/getleague/{country}")
        res = conn.getresponse()
        league = res.read()
        session['league'] = league
    except:
        league = "no response"
    flash(league)
    return redirect(url_for('index'))

# @app.route('/showLeague')
# def showLeague():
#     league = session.get('league')
#     # teams = list of teams from adams api
#     return render_template('showLeague.html', title='League Name', league=league)