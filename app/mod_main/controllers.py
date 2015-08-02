# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, session, redirect, url_for

from flask.ext.login import login_required

from app import app
from app.models import social

# Define the blueprint: 'main', set its url prefix: app.url/main
mod_main = Blueprint('main', __name__, url_prefix='/')

# Set the route and accepted methods
@mod_main.route('/', methods=['POST','GET'])
def index():
    return render_template("main/index.html")
