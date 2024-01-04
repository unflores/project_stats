import os

from flask import Flask
from flask_migrate import Migrate

from .api import api as api_blueprint
from .database import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('siteconfig.py')

    db.init_app(app)
    Migrate(app, db)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
