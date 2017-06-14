""" Database model file, describing the table schema used by Flask-SQLAlchemy """

from blackboard_api.database import db


# Representation of the Blackboard table
class Blackboard(db.Model):
    name = db.Column(db.String(32), primary_key=True)
    message = db.Column(db.String(255))
    status = db.Column(db.Boolean)

    def __init__(self, name, message='', status=True):
        self.name = name
        self.message = message
        self.status = status

    def __repr__(self):
        return '{''name'': {}, ''message'': {}, ''status'': {}}' % self.name, self.message, self.status
