# -*- coding: utf-8 -*-
# Import flask and template operators
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_triangle import Triangle

# Define the WSGI application object
app = Flask(__name__)
Triangle(app)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from app.mod_administrator.controllers import mod_administrator as admin_module

app.register_blueprint(admin_module)