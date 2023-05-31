#!/usr/bin/python3
"""
create a route /status on the object app_views that returns a JSON
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def get_status():
    """ get status """
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """ get app stats """
    stats = {}
    stat_obj = {
            'amenities': 'Amenity',
            'cities': 'City',
            'places': 'Place',
            'reviews': 'Review',
            'states': 'State',
            'users': 'User'
    }
    for key, value in stat_obj.items():
        stats[key] = storage.count(value)
    return jsonify(stats)
