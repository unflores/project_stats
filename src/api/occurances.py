from flask import jsonify
from . import api
import datetime

@api.route('/occurances/<string:type>')
def get_occurances(type):
  return jsonify([[datetime.datetime(2010, 10, 10).isoformat(), 1]])
