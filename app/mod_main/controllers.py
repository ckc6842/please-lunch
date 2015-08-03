# Import flask dependencies
from flask import Blueprint, render_template

from flask.ext.login import login_required

from app import social, app


# Define the blueprint: 'main', set its url prefix: app.url/main
mod_main = Blueprint('main', __name__, url_prefix='/')


# Set the route and accepted methods
@mod_main.route('/', methods=['POST', 'GET'])
def index():
    return render_template("main/index.html")


@app.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    return render_template('main/profile.html')

