from website import db
from flask_login import UserMixin
from datetime import datetime


class userCredentials(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
    loginTime = db.Column(db.Boolean())
