from flask import Flask

from routes import api
from serializers import configure as config_ma


def start():
    app = Flask("ClimaTempo")

    config_ma(app)

    app.register_blueprint(api)

    app.run()


if __name__ == '__main__':
    start()
