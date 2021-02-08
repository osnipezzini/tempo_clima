from flask import Flask
from flask_migrate import Migrate

from config import CONNECTION_STRING
from database import init_db
from routes import api
from serializers import init_marshmallow


def create_app():
    _app = Flask(__name__)
    _app.config['SQLALCHEMY_DATABASE_URI'] = CONNECTION_STRING
    _app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_marshmallow(_app)
    init_db(_app)

    Migrate(_app, _app.db)
    _app.register_blueprint(api)
    return _app


app = create_app()
