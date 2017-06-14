import logging.config
from logging.handlers import RotatingFileHandler
from time import strftime

from flask import Flask, Blueprint, request, jsonify

from blackboard_api import settings
from blackboard_api.api_1_0.blackboard import ns as blackboard
from blackboard_api.api_1_0.restplus import api
from blackboard_api.database import db

app = Flask(__name__)

handler = RotatingFileHandler('app.log', maxBytes=1000000, backupCount=3)
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(handler)


@app.errorhandler(404)
def not_found(error):
    return jsonify(error=str(error)), 404


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


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    api.init_app(blueprint)
    api.add_namespace(blackboard)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)


def main():
    initialize_app(app)
    app.run(debug=settings.FLASK_DEBUG, host=settings.FLASK_HOST, port=settings.FLASK_PORT)


if __name__ == '__main__':
    main()
