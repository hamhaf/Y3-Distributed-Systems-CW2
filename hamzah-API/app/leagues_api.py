from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from app import models, db
import json

app = Flask(__name__)
api = Api(app)

class League(Resource):

    def get(self, country):
        league = League.Property.query.filter_by(league_name = country).first()
        dict = {'country' : country,
                'league' : league}
        league = json.dump(dict)
        return league

    def post(self, league, country):
        
        return json

    def put(self, league):
        return json

    def delete(self, league=None, id=None):
        return json
