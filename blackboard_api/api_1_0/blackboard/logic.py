""" Implementation (business logic) of the required functionality """

from flask_restplus import marshal
from sqlalchemy import exc

from blackboard_api.api_1_0.blackboard import http
from blackboard_api.api_1_0.blackboard.serializer import *
from blackboard_api.database import db
from blackboard_api.database.models import Blackboard


# Implementation of the CREATE_BLACKBOARD requirement.
def create_blackboard(name):
    blackboard_entity = Blackboard(name)
    try:
        db.session.add(blackboard_entity)
        db.session.commit()
    # Catch error from SQLAlchemy:
    except exc.IntegrityError:
        return marshal({'response': http.PUT_RESPONSE_409}, http_response), 409

    return marshal({'response': http.PUT_RESPONSE_201}, http_response), 201


# Implementation of the DISPLAY_BLACKBOARD requirement.
def display_blackboard(name, payload):
    message = payload.get('message')
    try:
        blackboard_entity = Blackboard.query.filter_by(name=name).first()
        blackboard_entity.message = message
        blackboard_entity.status = False
        db.session.commit()
    except AttributeError:
        return marshal({'response': http.RESPONSE_404}, http_response), 404

    return marshal({'response': http.POST_RESPONSE_201}, http_response), 201


# Implementation of the READ_BLACKBOARD requirement.
def read_blackboard(name):
    try:
        blackboard_entity = Blackboard.query.filter_by(name=name).first()
        message = blackboard_entity.message
        if message == '':
            return marshal({'response': http.GET_RESPONSE_409}, http_response), 409
    except AttributeError:
        return marshal({'response': http.RESPONSE_404}, http_response), 404

    return marshal({'response': http.GET_RESPONSE_200, 'message': str(message)}, http_message), 200


# Implementation of the CLEAR_BLACKBOARD requirement.
def clear_blackboard(name):
    try:
        blackboard_entity = Blackboard.query.filter_by(name=name).first()
        blackboard_entity.message = ''
        blackboard_entity.status = True
        db.session.commit()
    except AttributeError:
        return marshal({'response': http.RESPONSE_404}, http_response), 404

    return marshal({'response': http.PATCH_RESPONSE_200}, http_response), 200


# Implementation of the GET_BLACKBOARD_STATUS requirement.
def get_blackboard_status(name):
    try:
        blackboard_entity = Blackboard.query.filter_by(name=name).first()
        status = blackboard_entity.status
    except AttributeError:
        return marshal({'response': http.RESPONSE_404}, http_response), 404

    return marshal({'response': http.GET_RESPONSE_200, 'isEmpty': status}, http_status), 200


# Implementation of the DELETE_BLACKBOARD requirement.
def delete_blackboard(name):
    if Blackboard.query.filter_by(name=name).scalar() is not None:
        Blackboard.query.filter_by(name=name).delete()
        db.session.commit()
    else:
        return marshal({'response': http.RESPONSE_404}, http_response), 404

    return marshal({'response': http.DELETE_RESPONSE_200}, http_response), 200


# To be implemented: optionally defined READ_ALL_BLACKBOARDS requirement.
def read_all_blackboards(name):
    pass


# Implementation of the optionally defined DELETE_ALL_BLACKBOARDS requirement.
def delete_all_blackboards():
    Blackboard.query.delete()
    db.session.commit()
    return marshal({'response': http.DELETE_ALL_RESPONSE_200}, http_response), 200
