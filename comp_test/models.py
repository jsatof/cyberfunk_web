from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Scores(UserMixin, db.Model):
    scoreid = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(100), unique=True)
    score = db.Column(db.Integer)
    combo = db.Column(db.String(1000))
    perfects = db.Column(db.String(1000))
    greats = db.Column(db.String(1000))
    goods = db.Column(db.String(1000))
    misses = db.Column(db.String(1000))
    uid = db.Column(db.Integer)
    