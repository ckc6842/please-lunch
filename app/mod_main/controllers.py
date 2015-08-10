# Import flask dependencies
from flask import Blueprint, render_template
from flask.ext.login import login_required


# Define the blueprint: 'main', set its url prefix: app.url/main
mod_main = Blueprint('main', __name__, url_prefix='')


# Set the route and accepted methods
@mod_main.route('/', methods=['POST', 'GET'])
def index():
    # print user_datastore.create_role(name='User', description='Generic user')
    # user_datastore.add_role_to_user(current_user, 'admin')
    # user_datastore.commit()
    return render_template("main/index.html")


@mod_main.route('/recommend', methods=['GET'])
@login_required
def recommend():
    return render_template('404.html')


@mod_main.route('/recommend/evaluate', methods=['POST', 'GET'])
@login_required
def evaluate():
    return render_template('404.html')


@mod_main.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    return render_template('main/profile.html')