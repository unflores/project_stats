import datetime
from flask import Blueprint
from flask import jsonify

occurances = Blueprint('occurances', __name__)

@occurances.route('/occurances/<string:filter_type>')
# pylint: disable-next=unused-argument
def list_occurances(filter_type):
    """Return a list of occurances  """
    return jsonify([[datetime.datetime(2010, 10, 10).isoformat(), 1]])
