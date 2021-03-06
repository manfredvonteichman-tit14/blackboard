#!/usr/bin/env python

""" This is the base class to start the RESTful web service hosting the Blackboard API. """

import logging.config
from logging.handlers import RotatingFileHandler
from time import strftime

from flask import Flask, Blueprint, request, jsonify

from blackboard_api import settings
from blackboard_api.api_1_0.blackboard import ns as blackboard
from blackboard_api.api_1_0.restplus import api
from blackboard_api.database import db

__author__ = 'Manfred von Teichman'
__version__ = '1.0'
__maintainer__ = 'Manfred von Teichman'
__email__ = 'vonteichman.m-tit14@it.dhbw-ravensburg.de'
__status__ = 'Development'

app = Flask(__name__)

# Setup the logging functionality
handler = RotatingFileHandler('app.log', maxBytes=1000000, backupCount=3)
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(handler)


# Catch any 404 error and return it as a json response
@app.errorhandler(404)
def not_found(error):
    return jsonify(error=str(error)), 404


# Registers the logging functionality to run after each request.
@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    log.info('%s %s %s %s %s %s',
             timestamp, request.remote_addr, request.method,
             request.scheme, request.full_path, response.status)
    return response


def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


# Create the app using a factory, setup its dependencies and the base url given the set prefix.
def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    api.init_app(blueprint)
    api.add_namespace(blackboard)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)


# Initialize the app and run it on the pre-configured hostname and port.
def main():
    initialize_app(app)
    app.run(debug=settings.FLASK_DEBUG, host=settings.FLASK_HOST, port=settings.FLASK_PORT)


if __name__ == '__main__':
    main()
