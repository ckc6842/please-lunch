# -*- coding: utf-8 -*-
# Import flask and template operators
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_triangle import Triangle
from flask_mail import Mail
from flask_babel import Babel
from flask.ext.login import LoginManager
from flask.ext.security import AnonymousUser
from flask_jsglue import JSGlue
from celery import Celery
import re

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

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
from app.models import *

# register flask ext
Triangle(app)
mail = Mail(app)
babel = Babel(app)
jsglue = JSGlue(app)

# Setup flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.user_loader(load_user)
login_manager.anonymous_user = AnonymousUser
login_manager.login_view = "/login"

# config celery with flask
def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('error/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error/500.html'), 500

# can print template's filename in HTML title tag
@app.template_filter('quoted')
def quoted(s):
    l = re.findall('\'([^\']*)\'', str(s))
    if l:
        return l[0]
    return None

# 샐러리 초기화
celery = make_celery(app)

# Import a module
from app.views.main import MainView
from app.views.start import StartView
from app.views.auth import *
from app.views.admin import AdminView

MainView.register(app)
StartView.register(app)
AuthView.register(app)
AdminView.register(app)
LeaveView.register(app)
DeleteUserView.register(app)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
