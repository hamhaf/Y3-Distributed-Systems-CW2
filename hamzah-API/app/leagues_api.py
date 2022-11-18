from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from app import models, db
import json

app = Flask(__name__)
api = Api(app)

class GetLeague(Resource):

    def get(self, country):
        country = "England"
        league = models.League.query.filter_by(country = country).first()
        dict = {'country' : country,
                'league' : league}
        print(f"returned {league}")
        print(league)
        league = json.dumps(dict)
        
        return league

class PostLeague(Resource):

    def post(self, league, country):
        item = models.League(league_name=league, country=country)
        db.session.add(item)
        db.session.commit()
        posted = {'country' : country,
                'league' : league}
        print(f"posted '{posted}' to the db")
        print(posted)
        posted = json.dumps(posted)
        
        return posted


class PutLeague(Resource):

    def put(self, old_league, new_league):
        league = models.League.query.filter_by(league_name = old_league).first()
        league.league_name = new_league
        db.session.commit()
        print (f"changed '{old_league}' to '{new_league}'")
        print(changed)
        changed = {'old_league':old_league,
                    'new_league':new_league}
        changed = json.dumps(changed)
        
        return changed


class DeleteLeague(Resource):

    def delete(self, id):
        models.League.query.filter_by(id = id).delete()
        deleted = {'deleted':id}
        deleted = json.dumps(deleted)
        print(f"deleted record with id: {id}")
        print(deleted)
        return deleted

api.add_resource(GetLeague, '/league/getleague/<string:country>')
api.add_resource(PostLeague, '/league/postleague/<string:league>&<string:country>')
api.add_resource(PutLeague, '/league/putleague/<string:old_league>&<string:new_league>')
api.add_resource(DeleteLeague, '/league/deleteleague/<int:id>')
