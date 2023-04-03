from website import db
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.sql import func

"""
class ClientProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
"""

class userCredentials(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
    loginTime = db.Column(db.Boolean())
    profile = db.relationship('ClientProfile')
