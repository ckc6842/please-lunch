# -*- coding: utf-8 -*-

# Import flask dependencies
from flask import render_template, redirect, url_for
from flask_classy import FlaskView
from flask.ext.login import login_required, current_user
from flask_security.forms import LoginForm, RegisterForm
from app.models import user_datastore


class MainView(FlaskView):
    route_base = '/'

    # 현재 로그인 한 유저에게 role 추가하는 코드
    if current_user.is_authenticated():
        user_datastore.create_role(name='admin',description='Admin user')
        user_datastore.add_role_to_user(current_user, 'admin')
        db.session.commit()

    def index(self):
        loginform = LoginForm()
        registerform =  RegisterForm()

        if not current_user.is_authenticated():
            # 로그인을 아예 안 함.
            return render_template("main/index.html", login_user_form = loginform, register_user_form = registerform)
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
        return render_template('main/recommend.html')