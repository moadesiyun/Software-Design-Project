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
    fuelquote = db.relationsip('fuelQuote', backref="user_credentials2", uselist=False)

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
    #Setting as parent to fuelQuote
    fuelQuoteID = db.relationship('QuoteForm', backref='profile')


class fuelQuote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gallonsRequested = db.column(db.integer)
    suggestedPPG = db.column(db.integer)
    #Boolean value stored as: 0:FALSE 1:TRUE
    #Default set to "new customer" 
    previousUserStatus = db.column(db.integer, default=0)
    TotalAmountDue = db.column(db.integer)

    #Setting child ID as child column
    profile_id = db.Column(db.integer, db.ForeignKey('profile.id'), nullable=False)
    usercredentials = db.Column(db.integer, db.ForeignKey('user_credentials2'), unique=True, nullable=False)

