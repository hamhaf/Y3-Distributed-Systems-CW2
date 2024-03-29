from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from app import models, db, app

# parser = reqparse.RequestParser()
# parser.add_argument('id')
# parser.add_argument('league')
# parser.add_argument('country')



api = Api(app)

class GetLeague(Resource):

    def get(self, country):
        league = models.League.query.filter_by(country = country).first()#.league_name
        if league != None:
            league_name = league.league_name
            dict = {'id':league.id,
                    'country' : country,
                    'league' : league_name}
            print(f"returned {league_name}")
            return dict, 201
        else:
            dict = {'error':f'could not find the first division league in {country}'}
            print(f"could not find the first division league in {country}")
            abort(404, description=dict['error'])

class PostLeague(Resource):

    # def __init__(self):
    #     self.league = parser.parse_args().get('league',None)
    #     self.country = parser.parse_args().get('country',None)
        

    def post(self, league, country):
        # args = parser.parse_args()
        # league = args['league']
        # country = args['country']
        item = models.League(league_name=league, country=country)
        message = f"item.league_name = {item.league_name}, item.country = {item.country}"
        print(message)
        if item.league_name and item.country:
            db.session.add(item)
            db.session.commit()
            id = models.League.query.filter_by(country = country).first().id
            posted = {'id' : id,
                    'country' : country,
                    'league' : league}
            print(f"posted '{posted}' to the db")
            return posted, 201
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

    def put(self, recordID, league, country):
        # args = parser.parse_args()
        # recordID = args['id']
        # league = args['league']
        # country = args['country']
        
        record = models.League.query.filter_by(id = recordID).first()
        if record != None:
            record.league_name = league
            record.country = country
            db.session.commit()
            print (f"updated to '{league}' and '{country}'")
            changed = {'league':league,
                        'country':country}
            print(changed)
            return changed
        else:
            message = f"could not find id \'{recordID}\'"
            print(message)
            return {"message":message}


class DeleteLeague(Resource):

    def delete(self, recordID):
        # args = parser.parse_args()
        # recordID = args['id']
        record = models.League.query.filter_by(id = recordID)
        if record.first() is not None:
            league_name = record.first().league_name
            country = record.first().country
            record.delete()
            db.session.commit()
            deleted = {'deleted':{"league":league_name,"country":country}}
            print(f"deleted record with id: {recordID}")
            print(deleted)
        else:
            deleted = {'message':f'could not find record with id {recordID}'}
            print(deleted)
        return deleted

api.add_resource(GetLeague, '/league/getleague/<string:country>')
api.add_resource(PostLeague, '/league/postleague/<string:league>/<string:country>')
api.add_resource(PutLeague, '/league/putleague/<int:recordID>/<string:league>/<string:country>')
api.add_resource(DeleteLeague, '/league/deleteleague/<int:recordID>')
