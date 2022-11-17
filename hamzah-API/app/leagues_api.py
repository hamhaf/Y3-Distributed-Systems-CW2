from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from app import models, db
import json

app = Flask(__name__)
api = Api(app)

class GetLeague(Resource):

    def get(self, country):
        league = models.League.Property.query.filter_by(country = country).first()
        dict = {'country' : country,
                'league' : league}
        league = json.dumps(dict)
        print(f"returned {league}")
        return league

class PostLeague(Resource):

    def post(self, league, country):
        item = models.League(league_name="Premier League", country="England")
        db.session.add(item)
        db.session.commit()
        posted = {'country' : country,
                'league' : league}
        posted = json.dumps(posted)
        print(f"posted '{posted}' to the db")
        return posted


class PutLeague(Resource):
    def put(self, old_league, new_league):
        league = models.League.Property.query.filter_by(league_name = old_league).first()
        league.league_name = new_league
        db.session.commit()
        print (f"changed '{old_league}' to '{new_league}'")
        changed = {'old_league':old_league,
                    'new_league':new_league}
        changed = json.dumps(changed)
        return changed

class DeleteLeague(Resource):
    def delete(self, league=None, id=None):
        return json

api.add_resource(League, )