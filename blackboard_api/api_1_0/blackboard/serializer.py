""" Custom model definition used to marshal and for the Swagger UI documentation """

from flask_restplus import fields

from blackboard_api.api_1_0.restplus import api

blackboard = api.model('BlackboardResource', {
    'name': fields.String(required=True, description='The name and unique identifier of a blackboard resource'),
    'message': fields.String(required=True, description='The message of the blackboard resource'),
    'status': fields.Boolean(required=False, readonly=False, default=False,
                             description='The status of the blackboard resource'),
})

# Model is used to marshal any returned blackboard messages.
blackboard_message = api.model('BlackboardMessage', {
    'message': fields.String(required=True, min_length=1, max_length=255,
                             description='The message of the blackboard resource'),
})

# Model is used to marshal any returned custom HTTP responses.
http_response = api.model('CustomHttpResponse', {
    'response': fields.String(required=True, description='Custom HTTP response message.'),
})

# Model is used to marshal any returned custom HTTP responses including a message field.
http_message = api.model('CustomHttpMessage', {
    'response': fields.String(required=True, description='Custom HTTP response message.'),
    'message': fields.String(required=True, description='The message of the blackboard resource'),
})

# Model is used to marshal any returned custom HTTP response including a isEmpty field.
http_status = api.model('CustomHttpStatus', {
    'response': fields.String(required=True, description='Custom HTTP response message.'),
    'isEmpty': fields.Boolean(required=True, description='Blackboard status data from the Blackboard API.'),
})

# Model is used to marshal specially returned custom HTTP error responses.
http_error = api.model('CustomHttpError', {
    'message': fields.String(required=True, description='Message for internal error'),
})
