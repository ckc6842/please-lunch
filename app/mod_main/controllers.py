# Import flask dependencies
from flask import Blueprint, render_template
from flask.ext.login import login_required, current_user

from app import app

from app.models import user_datastore

# Define the blueprint: 'main', set its url prefix: app.url/main
mod_main = Blueprint('main', __name__, url_prefix='')


# Set the route and accepted methods
@mod_main.route('/', methods=['POST', 'GET'])
def index():
    return render_template("main/index.html")


@mod_main.route('/recommend', methods=['GET'])
@login_required
def recommend():
    return render_template('404.html')


@mod_main.route('/recommend/evaluate', methods=['POST', 'GET'])
@login_required
def evaluate():
    return render_template('404.html')
