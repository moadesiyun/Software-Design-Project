from website import db
from flask_login import UserMixin
from datetime import datetime


class ClientDB(db.Model, UserMixin):
    Id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
    loginTime = db.Column(db.DateTime())
