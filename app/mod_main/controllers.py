# -*- coding: utf-8 -*-

# Import flask dependencies
from flask import Blueprint, render_template, redirect, url_for
from flask.ext.login import login_required, current_user


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


@mod_main.route('/recommend/evaluate', methods=['POST', 'GET'])
@login_required
def evaluate():
    return render_template('404.html')