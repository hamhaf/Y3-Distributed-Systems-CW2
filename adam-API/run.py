from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import http.client
import time, numpy as np



app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///team.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class Team(db.Model):
    teamname = db.Column(db.String(80), primary_key=True)
    league = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"{self.teamname} - {self.league}"


class GetTeam(Resource):
    def get(self, teamname):
        teams = Team.query.filter_by(league=teamname).all()
        team_list = []
        for x in teams:
            team_data = {'teamname': x.teamname, 'league': x.league}
            team_list.append(team_data)

        return {"Teams": team_list}



class AddTeam(Resource):
    def post(self,teamname,league):

        data = Team(teamname, league)
        db.session.add(data)
        db.session.commit()
        print("Team Added Successfully")
        return make_response(jsonify({'team':data.teamname, 'league': data.league}),201)
        

class UpdateTeam(Resource):
    def put(self,primary,teamname,league):
        tm = Team.query.get(primary)
        if tm is None:
            return {'error': 'not found'}, 404
        else:
            tm.teamname = teamname
            tm.league = league
            db.session.commit()
            return "Team Updated"


class DeleteTeam(Resource):
    def delete(self,teamname):
        tm = Team.query.get(teamname)
        if tm is None:
            return {'error': 'not found'}, 404

        db.session.delete(tm)
        db.session.commit()
        return "Team Deleted"


api.add_resource(GetTeam, '/team/<string:teamname>')
api.add_resource(AddTeam, '/team/add/<string:teamname>/<string:league>')
api.add_resource(UpdateTeam, '/team/update/<string:primary>/<string:teamname>/<string:league>')
api.add_resource(DeleteTeam, '/team/delete/<string:teamname>')



conn = http.client.HTTPConnection("127.0.0.1:8002")
conn.request("GET",f"/team/Bundesliga")
res = conn.getresponse()



n=5
results = []
for x in range(1,n+1):
    start = time.time()
    conn = http.client.HTTPConnection("127.0.0.1:8002")
    conn.request("GET",f"/team/Bundesliga")
    res = conn.getresponse()
    conn.request("POST",f"/team/add/Adamfc/Bundesliga")
    res = conn.getresponse()
    conn.request("PUT",f"/team/update/Adamfc/Adamfc/Premier League")
    res = conn.getresponse()
    conn.request("DELETE",f"/team/delete/Adamfc")
    res = conn.getresponse()
    end = time.time()
    elapsed = end -start
    print(x)
    results.append(elapsed)


print(f"avg = {np.mean(results)}")
print(f"std = {np.std(results)}")

if __name__ == '__main__':
    app.run(debug=True)



