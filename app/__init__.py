# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

from flask_mail import Mail

from flask.ext.login import LoginManager
from flask.ext.security import Security, SQLAlchemyUserDatastore, AnonymousUser
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore
# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# facebook id
app.config['SOCIAL_FACEBOOK'] = {
    'consumer_key': '684002831732805',
    'consumer_secret': '51d173f01a0290682be0af5db48550a6'
}

app.config['SECURITY_POST_LOGIN'] = '/profile'

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
from app.models import *

# Setup Flask-Security

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
social = Social(app, SQLAlchemyConnectionDatastore(db, Connection))

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.anonymous_user = AnonymousUser

# mail setting
app.config['MAIL_SERVER'] = 'smtp.google.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'maxtortime@gmail.com'
app.config['MAIL_PASSWORD'] = 'password'
mail = Mail(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_main.controllers import mod_main as main_module

# Register blueprint(s)
app.register_blueprint(main_module)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
