from flask import Blueprint
from .occurances import occurances

api = Blueprint('api', __name__)
api.register_blueprint(occurances)
