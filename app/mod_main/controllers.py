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
    if not current_user.is_authenticated():
        # 로그인을 아예 안 함.
        return render_template("main/index.html")
    elif current_user.is_authenticated() and not current_user.is_evaluate:
        # 로그인은 했는데 평가를 안 함.
        return redirect(url_for('start.index'))
    elif current_user.is_authenticated() and current_user.is_evaluate:
        # 로그인도 하고 평가도 함.
        return redirect(url_for('main.recommend'))
    elif not current_user.confirmed_at:
        return render_template('main/confirm.html')
    else:
        # 아무것도 해당 안 됨.
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
def profile():
    return render_template('main/profile.html')


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
