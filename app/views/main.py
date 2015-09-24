# -*- coding: utf-8 -*-

# Import flask dependencies
from flask import render_template, redirect, url_for
from flask_classy import FlaskView
from flask.ext.login import login_required, current_user
from flask_security.forms import LoginForm, RegisterForm
from app.views.evaluate_user_score import evaluate_taste_score
from app.views.add_food_list import add_food_list
from app.views.Choice_food import choice_food

from app.models import Food, security
import random


# 로그인 렌더링 할때 dict으로 넘기면 추가적으로 매개변수를 줄수 있음
@security.login_context_processor
def security_login_context_processor():
    return dict(register_user_form=RegisterForm(), loginModalShow=True)


# 회원가입 렌더링 할때 dict으로 넘기면 추가적으로 매개변수를 줄수 있음
@security.register_context_processor
def security_register_context_processor():
    return dict(login_user_form=LoginForm(), registerModalShow=True)


class MainView(FlaskView):
    route_base = '/'

    # 현재 로그인 한 유저에게 role 추가하는 코드
    def index(self):
        loginform = LoginForm()
        registerform = RegisterForm()

        if not current_user.is_authenticated():
            # 로그인을 아예 안 함.
            return render_template("main/index.html", login_user_form=loginform, register_user_form=registerform)
        elif current_user.is_authenticated() and not current_user.is_evaluate:
            # 로그인은 했는데 평가를 안 함.
            return redirect(url_for('StartView:index'))
        elif current_user.is_authenticated() and current_user.is_evaluate:
            # 로그인도 하고 평가도 함.
            return redirect(url_for('MainView:recommend'))
        elif not current_user.confirmed_at:
            return render_template('main/confirm.html')
        else:
            # 아무것도 해당 안 됨.
            return render_template("main/index.html")

    @login_required
    def recommend(self):
        foods = Food.query.all()
        """
        recommend_food 가 작동하지 않을 경우 그냥 random으로 foodName을 가져온다.
        샐러리로 evaluate_user_score와 add_food_list를 3일마다 한번 실행시켜줘야함
        evaluate_user_score는 user_score Table에 user의 각종 데이터를 넣는 알고리즘
        add_food_list는 user_score를 가지고 음식10개를 최종 선발해주는 알고리즘
        choice_food는 add_food_list에서 뽑힌 10개의 음식리스트(user_food)에서 랜덤으로 하나 리턴해줌
        add_food_list 지금 버전에서는 시간대는 고려되지 않기때문에 Time Table에 Dummy Data를 넣어야 작동함
        """
        # food_name2 = evaluate_taste_score(current_user)
        # food_score = add_food_list(current_user)
        # food_name = random.choice(foods)

        try:
            food_name = choice_food(current_user)
        except:
            food_name = random.choice(foods)

        return render_template('main/recommend.html', food=food_name)
