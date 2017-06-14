""" The settings file used to pre-configure the Flask server """

__author__ = "Michał Karzyński"
__maintainer__ = "Manfred von Teichman"
__email__ = "vonteichman.m-tit14@it.dhbw-ravensburg.de"

# Flask settings
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 1337
FLASK_DEBUG = False  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///database/db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False
