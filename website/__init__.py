from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DATABASE = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'software-design proj'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE}'
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    from .requestForm import requestForm

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(requestForm, url_prefix='/')

    from .dbmodels import Client

    with app.app_context():
        db.create_all()
    
    return app

