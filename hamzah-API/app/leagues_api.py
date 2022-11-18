from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from app import models, db, app

parser = reqparse.RequestParser()
parser.add_argument('league')
parser.add_argument('country')

api = Api(app)

class GetLeague(Resource):

    def get(self, country):
        league = models.League.query.filter_by(country = country).first()#.league_name
        if league != None:
            league_name = league.league_name
            dict = {'country' : country,
                    'league' : league_name}
            print(f"returned {league_name}")
        else:
            dict = {'error':f'could not find the first division league in {country}'}
            print(f"could not find the first division league in {country}")
        return dict

class PostLeague(Resource):

    # def __init__(self):
    #     self.league = parser.parse_args().get('league',None)
    #     self.country = parser.parse_args().get('country',None)
        

    def post(self):
        args = parser.parse_args()
        league = args['league']
        country = args['country']
        item = models.League(league_name=league, country=country)
        message = f"item.league_name = {item.league_name}, item.country = {item.country}"
        print(message)
        if item.league_name and item.country:
            db.session.add(item)
            db.session.commit()
            posted = {'country' : country,
                'league' : league}
            print(f"posted '{posted}' to the db")
            return posted
        elif not item.league_name:
            # message = "please provide a league name"
            print(f"please provide a league name")
        elif not item.country:
            # message = "please provide a country"
            print(f"please provide a country")
        else:
            # message = "Error, please try again"
            print("Error, please try again")
        return {'message':message}

        


class PutLeague(Resource):

    def put(self, old_league, new_league):
        league = models.League.query.filter_by(league_name = old_league).first()
        league.league_name = new_league
        db.session.commit()
        print (f"changed '{old_league}' to '{new_league}'")
        print(changed)
        changed = {'old_league':old_league,
                    'new_league':new_league}
        
        return changed


class DeleteLeague(Resource):

    def delete(self, id):
        models.League.query.filter_by(id = id).delete()
        deleted = {'deleted':id}
        print(f"deleted record with id: {id}")
        print(deleted)
        return deleted

api.add_resource(GetLeague, '/league/getleague/<string:country>')
api.add_resource(PostLeague, '/league/postleague')
api.add_resource(PutLeague, '/league/putleague/<string:old_league>&<string:new_league>')
api.add_resource(DeleteLeague, '/league/deleteleague/<int:id>')
