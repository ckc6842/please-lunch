#-*- coding: utf-8 -*-

# Import flask dependencies
from flask import Blueprint, render_template, redirect, url_for, flash
from flask.ext.login import login_required, current_user, logout_user
from app.models import social, user_datastore
from forms import UserLeaveForm
from flask_security import roles_required
from flask_security.utils import verify_and_update_password


# Define the blueprint: 'main', set its url prefix: app.url/main
mod_main = Blueprint('main', __name__, url_prefix='')


# Set the route and accepted methods
@mod_main.route('/', methods=['POST', 'GET'])
def index():
    # user_datastore.create_role(name='User', description='Generic user')
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
    return render_template('main/profile.html', content='Profile Page', facebook_conn=social.facebook.get_connection())


@mod_main.route('/leave', methods=['POST', 'GET'])
@login_required
def leave():
    ispwcorrect = False
    form = UserLeaveForm()
    if form.validate_on_submit():
        if verify_and_update_password(form.password.data, current_user):
            flash("Your input is correct.")
            ispwcorrect = True
            user_datastore.create_role(name='leave', description='This user will be leave')
            user_datastore.add_role_to_user(current_user, 'leave')
            user_datastore.commit()

            render_template('main/leave.html', form=form, ispwcorrect=ispwcorrect)
        else:
            flash("Your input is not correct.")
            return redirect(url_for('main.leave'))
    return render_template('main/leave.html', form=form, ispwcorrect=ispwcorrect)


@mod_main.route('/delete', methods=['POST', 'GET'])
@login_required
@roles_required('leave')
def deleteuser():
    user_datastore.delete_user(current_user)
    logout_user()
    user_datastore.commit()
    return redirect(url_for('main.index'))
