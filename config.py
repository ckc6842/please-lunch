# Statement for enabling the development environment
DEBUG = True
WTF_CSRF_ENABLED = True
# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:n61cde5173@localhost/please_lunch'
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
SECRET_KEY = "secret"

# for flask-social
SOCIAL_FACEBOOK = {
    'consumer_key': '352785444846303',
    'consumer_secret': '2c7f62089ee65e73445366f7ce82f951'
}

SECURITY_POST_LOGIN = '/profile'
