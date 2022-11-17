from app import db

class League(db.Model):
    id = db.Column(db.Integer, primary_key=True) # makes id column to uniquely id each entry
    league_name = db.Column(db.String(200), nullable=False) #string field to store the user's input leaguename in the db
    country = db.Column(db.String(200), nullable=False)
