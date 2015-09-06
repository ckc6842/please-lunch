# Statement for enabling the development environment
DEBUG = True
WTF_CSRF_ENABLED = True
# Define the application directory
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example

if sys.platform == 'win32':
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/please-lunch'
    # celery db config
    CELERY_BROKER_URL = 'sqla+' + SQLALCHEMY_DATABASE_URI
    CELERY_RESULT_BACKEND = 'db+mysql+pymysql://root:1234@localhost/please-lunch'
else:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:n6!cfe5!73@localhost/please-lunch'
    # celery db config
    CELERY_BROKER_URL = 'sqla+' + SQLALCHEMY_DATABASE_URI
    CELERY_RESULT_BACKEND = 'db+mysql+pymysql://root:n6!cfe5!73@localhost/please-lunch'

DATABASE_CONNECT_OPTIONS = {}

# UPLOAD_FOLDER
UPLOAD_FOLDER = 'app/static/uploads/'

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "d41d8cd98f00b204e9800998ecf8427e"

# Secret key for signing cookies
SECRET_KEY = "super-secret"

SECURITY_REGISTERABLE =  True
SECURITY_CONFIRMABLE = False
SECURITY_TRACKABLE = True
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = 'X2LGFS1AI39VRWYCYMXG3L5F4GS8EE35WUB0YSVPX7SUFWP70ETI1G2ZV2LLQGJ8'
SECURITY_URL_PREFIX = ''
SECURITY_POST_LOGIN_VIEW = '/'
SECURITY_POST_REGISTER_VIEW = '/'


# for flask-social
SOCIAL_FACEBOOK = {
    'consumer_key': '684002831732805',
    'consumer_secret': '51d173f01a0290682be0af5db48550a6'
}

# Flask-SocialBlueprint
# https://github.com/wooyek/flask-social-blueprint
SOCIAL_BLUEPRINT = {
    # https://developers.facebook.com/apps/
    "flask_social_blueprint.providers.Facebook": {
        # App ID
        'consumer_key': '684002831732805',
        # App Secret
        'consumer_secret': '51d173f01a0290682be0af5db48550a6'
    },
    # https://apps.twitter.com/app/new
    "flask_social_blueprint.providers.Twitter": {
        # Your access token from API Keys tab
        'consumer_key': 'Us0qHlRupn9cRr2LgLanZQsCt',
        # access token secret
        'consumer_secret': 'jAm1UZEp4ckJAD9yErbUi7EBk0ayUbMPGwNIb7904Dq8bgROui'
    },
    # https://console.developers.google.com/project
    "flask_social_blueprint.providers.Google": {
        # Client ID
        'consumer_key': '435223545504-bgbqpavf8q157l8u5v2otvfg4khaqgeg.apps.googleusercontent.com',
        # Client secret
        'consumer_secret': '_GH1tElWK9tyk5KdppMZ5w3w'
    },
    # https://github.com/settings/applications/new
    "flask_social_blueprint.providers.Github": {
        # Client ID
        'consumer_key': 'c74d8b2d5b6448db33a5',
        # Client Secret
        'consumer_secret': '5e9e8e889dfe76a20e781a98eb0eb772c5f3ca30'
    },
}
