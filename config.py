# Statement for enabling the development environment
DEBUG = True
WTF_CSRF_ENABLED = True
# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:n61cde5173@localhost/please-lunch'

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
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "super-secret"
SECURITY_REGISTERABLE =  True
SECURITY_CONFIRMABLE = False
SECURITY_RECOVERABLE = False
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = 'abc'

MAIL_SERVER = 'smtp.google.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'pleaselunch8@gmail.com'
MAIL_PASSWORD = 'foxvkdlxld'
MAIL_USE_TLS = False

# for flask-social
SOCIAL_FACEBOOK = {
    'consumer_key': '686899584776463',
    'consumer_secret': '7d6b8e7257203c6e58c563718b30dfd0'
}

SECURITY_POST_LOGIN = '/profile'
