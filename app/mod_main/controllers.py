# Import flask dependencies
from flask import Blueprint, render_template
from flask.ext.login import login_required, current_user

from app import app

from app.models import user_datastore

# TODO: mod_main cannot route (.html 404)
# Define the blueprint: 'main', set its url prefix: app.url/main
mod_main = Blueprint('main', __name__, url_prefix='/', template_folder='templates/main')


# Set the route and accepted methods
@mod_main.route('/', methods=['POST', 'GET'])
def index():
    return render_template("main/index.html")


@mod_main.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    return render_template('main/profile.html')


@app.route('/test', methods=['POST', 'GET'])
@login_required
def test():
    return render_template('main/test.html')
