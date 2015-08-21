# -*- coding: utf-8 -*-
# Import flask and template operators
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_triangle import Triangle
from flask_mail import Mail
from flask_babel import Babel
from flask.ext.login import LoginManager
from flask.ext.security import AnonymousUser


# Define the WSGI application object
app = Flask(__name__)
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'pleaselunch8@gmail.com',
    MAIL_PASSWORD = 'foxvkdlxld',
))

Triangle(app)

mail = Mail(app)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
from app.models import *

# Setup Flask-Security

# Setup flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.user_loader(load_user)
login_manager.anonymous_user = AnonymousUser
login_manager.login_view = "/login"

babel = Babel(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable (mod_auth)

# Register blueprint(s)
from app.mod_main.controllers import mod_main as main_module
from app.mod_admin.controllers import mod_administrator as admin_module
from app.mod_start.controllers import mod_start as start_module
from app.mod_auth.controllers import mod_auth as auth_module

app.register_blueprint(admin_module)
app.register_blueprint(main_module)
app.register_blueprint(start_module)
app.register_blueprint(auth_module)
# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
