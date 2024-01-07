import os

from flask import Flask
from flask_migrate import Migrate

from .api import api as api_blueprint
from .database import db

# Bizarre but I have to load this to run db migrate
# There is probably a problem with the way I am struturing my models and db module
from .database import models  # noqa: F401

from .config import build_settings


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(build_settings())

    db.init_app(app)
    Migrate(app, db)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
