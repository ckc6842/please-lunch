# -*- coding: utf-8 -*-

# Import flask dependencies
from flask import Blueprint, render_template, redirect, url_for, flash
from flask.ext.login import login_required, current_user, logout_user
from app.models import social, user_datastore
from forms import UserLeaveForm
from app import db
from flask_security.utils import verify_and_update_password


# Define the blueprint: 'main', set its url prefix: app.url/main
mod_main = Blueprint('main', __name__, url_prefix='')


# 메인 화면
@mod_main.route('/', methods=['POST', 'GET'])
def index():
    # user_datastore.create_role(name='User', description='Generic user')
    # user_datastore.add_role_to_user(current_user, 'admin')
    # user_datastore.commit()
    return render_template("main/index.html")


# 음식 추천 요청
@mod_main.route('/recommend', methods=['GET'])
@login_required
def recommend():
    return render_template('main/recommend.html')


# GET: 추천받은 음식에 대한 감상을 묻는 페이지
# POST: 추천받은 음식 평가
@mod_main.route('/recommend/evaluate', methods=['POST', 'GET'])
@login_required
def evaluate():
    return render_template('404.html')


# 페이스북 연동용... 잘 안 됨.
@mod_main.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    return render_template('main/profile.html', content='Profile Page', facebook_conn=social.facebook.get_connection())


@mod_main.route('/leave', methods=['POST', 'GET'])
@login_required
def leave():
    is_pw_correct = False
    form = UserLeaveForm()
    if form.validate_on_submit():
        if verify_and_update_password(form.password.data, current_user):
            flash("Your input is correct.")
            is_pw_correct = True
            current_user.is_want_leave = True
            db.session.commit()
            return render_template('main/leave.html', form=form, is_pw_correct=is_pw_correct)
        else:
            flash("Your input is not correct.")
            return redirect(url_for('main.leave'))
    return render_template('main/leave.html', form=form, is_pw_correct=is_pw_correct)


@mod_main.route('/delete', methods=['POST', 'GET'])
@login_required
def deleteuser():
    if current_user.is_want_leave:
        user_datastore.delete_user(current_user)
        logout_user()
        user_datastore.commit()
        flash('Your account is successfully deleted!')
        return redirect(url_for('main.index'))
    else:
        flash('It is wrong approach!!!')
        return render_template('404.html')
