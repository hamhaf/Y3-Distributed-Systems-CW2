from flask import render_template, flash, request, redirect, url_for, g, session
from app import app
from .forms import CountryForm
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import exists
import os,time
from datetime import date
from werkzeug.utils import secure_filename
import http.client, json


@app.route('/')
def index():#the home page will be the login/sign up page
	form = CountryForm()
	return render_template('home.html', title='Country Select', form=form)#renders the home.html template passing the appropriate variabels

@app.route('/findLeague', methods=['POST','GET'])
def findLeague():
    form = CountryForm()
    country = form.country.data
    try:
        conn = http.client.HTTPConnection("127.0.0.1:8001")
        conn.request("GET",f"/league/getleague/{country}")
        res = conn.getresponse()
        league = json.loads(res.read().decode("utf-8"))['league']
        session['league'] = league
    except:
        league = "no response"
    flash(league)
    flash(f"res: {res}")
    return redirect(url_for('showLeague'))

@app.route('/showLeague')
def showLeague():
    league = session.get('league')
    leagueurl = league.replace(" ","%20")
    try:
        conn = http.client.HTTPConnection("127.0.0.1:8002")
        conn.request("GET",f"/team/{leagueurl}")
        res = conn.getresponse()
        teamsDict = json.loads(res.read().decode("utf-8"))['Teams']
        teams=[]
        for team in teamsDict:
            teams.append(team['teamname'])

        session['teams'] = teams
    except:
        teams = ['error']
    # teams = ['Manchester United', 'Liverpool', 'Real Madrid']
    return render_template('showLeague.html', title='League Name', league=league, teams = teams)

@app.route('/teamInfo/<team>')
def teamInfo(team):
    flash(team)
    team = team.replace(" ","%20")
    print(f"#### team = {team} ####")
    # external API call
    try:
        conn = http.client.HTTPSConnection("v3.football.api-sports.io")
        headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': "7070e4c98d8ff888e50ff23ce14d6c4c"
            }
        conn.request("GET", f"/teams?name={team}", headers=headers)

        res = conn.getresponse()
        data = json.loads(res.read().decode("utf-8"))
        flash(data)
        flash(f"res: {res}")
        session['data']=data
    except:
        data = {'response':[{'team':"no response"}]}
        print("error in teamInfo")
    return redirect(url_for('showInfo'))

@app.route('/showInfo')
def showInfo():
    print(f"data  = {session.get('data')} in showInfo")
    data = session.get('data')['response'][0]['team']
    name = data['name']
    code = data['code']
    country = data['country']
    founded = data['founded']
    national = data['national']
    logo = data['logo']
        
    return render_template('teamInfo.html', title='Team Info', data=data, name=name, 
                            code=code, country=country, founded=founded, national=national, logo=logo)