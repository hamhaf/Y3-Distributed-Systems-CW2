from config import SQLALCHEMY_DATABASE_URI
from app import db, models
import os.path

db.create_all() #creates the db tables
object = models.League(league_name="Premier League")
db.session.add(object)
db.session.commit()