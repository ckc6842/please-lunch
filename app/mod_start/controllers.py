from flask import Blueprint, render_template, redirect, url_for, flash, jsonify
from flask_security import login_required, current_user
from app import db

# Define the blueprint: 'start', set its url prefix: app.url/start
mod_start = Blueprint('start', __name__, url_prefix='/start')


@mod_start.route('/', methods=['GET'])
@login_required
def index():
    if current_user.is_evaluate:
        return redirect(url_for('main.recommend'))
    else:
        return render_template('start/index.html')


@mod_start.route('/info', methods=['POST'])
@login_required
def info():
    if not current_user.is_evaluate:
        current_user.is_evaluate = True
        db.session.commit()
    else:
        flash('You are already evaluated')
        return redirect(url_for('main.recommend'))

    return redirect(url_for('start.evaluate'))


@mod_start.route('/evaluate', methods=['POST', 'GET'])
@login_required
def evaluate():
    flash('Your information successfully evaluated!')
    return redirect(url_for('main.recommend'))

@mod_start.route('/getfoodlist', methods=['POST', 'GET'])
@login_required
def getfoodlist():
    return jsonify({'id': 1, 'foodName' : 'apple'}, {'id' : 2, 'foodName' : 'banana'})
