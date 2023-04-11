from website import db
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.sql import func


class userCredentials(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
    loginTime = db.Column(db.Boolean())

    #Setting as parent to profile
    profile = db.relationship('Profile', backref='user_credentials', uselist=False)
    #Setting as parent to fuelQuote
    fuelquotes = db.relationship('fuelQuote', backref='user_credentials')

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    address1 = db.Column(db.String(100), nullable=False)
    address2 = db.Column(db.String(100))
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zipcode = db.Column(db.String(9), nullable=False)
    # Foreign key to link to User model
    user_id = db.Column(db.Integer, db.ForeignKey('user_credentials.id'), unique=True, nullable=False)


class fuelQuote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gallons = db.Column(db.Integer,nullable=False)
    sugppg = db.Column(db.Integer,nullable=False)
    date = db.Column(db.String(20), nullable=False)
    delivery_date = db.Column(db.String(20), nullable=False)
    #Boolean value stored as: 0:FALSE 1:TRUE
    #Default set to "new customer" 
    ##previous_status = db.Column(db.Integer)
    totaldue = db.Column(db.Integer, nullable=False)

    #Setting child ID as child column
    user_id = db.Column(db.Integer, db.ForeignKey('user_credentials.id'), nullable=False)
