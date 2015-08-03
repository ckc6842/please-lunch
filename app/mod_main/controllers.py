# Import flask dependencies
from flask import Blueprint, render_template
from app import app


# Define the blueprint: 'main', set its url prefix: app.url/main
mod_main = Blueprint('main', __name__, url_prefix='/')


# Set the route and accepted methods
@mod_main.route('/', methods=['POST', 'GET'])
def index():
    return render_template("main/index.html")


@app.route('/profile', methods=['POST', 'GET'])
def profile():
    return render_template('main/profile.html')

