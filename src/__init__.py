import os

from flask import Flask
from .api import api as api_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('siteconfig.py')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(api_blueprint, url_prefix='/api')


    return app
