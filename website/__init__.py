from flask import Flask
from os import path


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'software-design proj'
    from .views import views
    from .auth import auth
    from .requestForm import requestForm

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(requestForm, url_prefix='/')

    
    return app

