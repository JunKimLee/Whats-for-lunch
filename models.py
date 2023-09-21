from . import db

class Cusine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))

# Set up recipies database model
class Recipies(db.Model):
    Cusineid = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    link = db.Column(db.String(150))