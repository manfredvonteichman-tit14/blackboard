""" Flask-RESTPlus initialization """

from flask_restplus import Api

# Setup the Flask-RESTPlus Api, Swagger UI and more.
api = Api(version='1.0', title='Blackboard API',
          description='A RESTful web service providing the Blackboard API')
