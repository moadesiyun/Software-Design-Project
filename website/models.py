from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    userAddress1 = db.Column(db.String(100))
    userAddress2 = db.Column(db.String(100))
    city = db.Column(db.String(15))
    state  = db.Column(db.String(2))
    zipcode = db.Column(db.Integer())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(150))
