from flask import Flask

from routes import api


def start():
    app = Flask("ClimaTempo")

    app.register_blueprint(api)

    app.run()


if __name__ == '__main__':
    start()
