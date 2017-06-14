from flask import request
from flask_restplus import Resource

from blackboard_api.api_1_0.blackboard import http
from blackboard_api.api_1_0.blackboard.logic import *
from blackboard_api.api_1_0.blackboard.serializer import *
from blackboard_api.api_1_0.restplus import api

ns = api.namespace('blackboard', description='Operations related to the blackboard resources')


@ns.route('/')
@api.response(500, http.RESPONSE_500, http_error)
class BlackboardCollection(Resource):
    @api.response(200, http.DELETE_RESPONSE_200, http_response)
    def delete(self):
        """
        Delete the complete blackboard collection.
        """
        return delete_all_blackboards()

@ns.route('/<name>')
@api.response(500, http.RESPONSE_500, http_error)
class BlackboardResource(Resource):
    @api.response(201, http.PUT_RESPONSE_201, http_response)
    @api.response(409, http.PUT_RESPONSE_409, http_response)
    def put(self, name):
        """
        Create a new named blackboard instance.
        """
        return create_blackboard(name)

    @api.expect(blackboard_message)
    @api.response(201, http.POST_RESPONSE_201, http_response)
    @api.response(400, http.RESPONSE_400)
    @api.response(404, http.RESPONSE_404, http_response)
    def post(self, name):
        """
        Display the message of the named blackboard instance.
        """
        return display_blackboard(name, payload=request.json)

    @api.response(200, http.GET_RESPONSE_200, http_message)
    @api.response(404, http.RESPONSE_404, http_response)
    @api.response(409, http.GET_RESPONSE_409, http_response)
    def get(self, name):
        """
        Read message of named blackboard instance.
        """
        return read_blackboard(name)

    @api.response(200, http.DELETE_RESPONSE_200, http_response)
    @api.response(404, http.RESPONSE_404, http_response)
    def delete(self, name):
        """
        Delete named blackboard instance.
        """
        return delete_blackboard(name)


@ns.route('/<name>/status')
@api.response(500, http.RESPONSE_500, http_error)
class BlackboardResourceStatusController(Resource):
    @api.response(200, http.GET_RESPONSE_200, http_status)
    @api.response(404, http.RESPONSE_404, http_response)
    def get(self, name):
        """
        Retrieve status of named blackboard instance.
        """
        return get_blackboard_status(name)


@ns.route('/<name>/clear')
@api.response(500, http.RESPONSE_500, http_error)
class BlackboardResourceClearController(Resource):
    @api.response(200, http.PATCH_RESPONSE_200, http_response)
    @api.response(404, http.RESPONSE_404, http_response)
    def patch(self, name):
        """
        Clear message of named blackboard instance.
        """
        return clear_blackboard(name)
