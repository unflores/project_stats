from flask import jsonify
from flask import current_app


import datetime

@current_app.route('/occurances/<string:type>')
def get_occurances(type):
  return jsonify([[datetime.datetime(2010, 10, 10).isoformat(), 1]])
