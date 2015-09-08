# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, \
    flash, request, after_this_request
from flask_classy import FlaskView, route
from flask.ext.login import current_user
from flask_security.utils import verify_and_update_password, logout_user, login_user, \
    get_post_login_redirect, url_for_security
from flask_security.decorators import anonymous_user_required, login_required
from werkzeug.datastructures import MultiDict

from flask_security.forms import LoginForm

from app.utils import _render_json, _commit, _ctx
from app.models import security,user_datastore
from app.forms import UserLeaveForm
from app import db

__author__ = 'maxto'


class AuthViewMin(FlaskView):
    route_prefix = '/auth/'


class LoginView(AuthViewMin):
    route_base = '/login/'
    decorators = [anonymous_user_required]
    form_class = security.login_form

    def index(self):
        form = self.form_class()

        return render_template('security/login_user.html', login_user_form=form)

    def post(self):
        if request.json:
            login_form = self.form_class(MultiDict(request.json))
        else:
            login_form = self.form_class()

        if login_form.validate_on_submit():
            login_user(login_form.user, remember=login_form.remember.data)
            after_this_request(_commit)

            if not request.json:
                return redirect(get_post_login_redirect(login_form.next.data))

            if request.json:
                return _render_json(login_form, include_auth_token=True)

            return redirect(url_for('MainView:index'))
        else:
            print "no"
            for field in login_form:
                if field.errors:
                    for error in field.errors:
                        print error
            return render_template('temperror.html', login_form=login_form)


class LogoutView(AuthViewMin):
    route_base = '/logout/'
    #decorators = [login_required]

    def index(self):
        if current_user.is_authenticated():
            logout_user()

        return redirect(url_for('MainView:index'))


class AuthView(AuthViewMin):
    decorators = [login_required]

    def profile(self):
        return render_template('main/profile.html')


class LeaveView(AuthViewMin):
    decorators = [login_required]

    def get(self):
        form = UserLeaveForm()
        is_pw_correct = False
        return render_template('main/leave.html', form=form, is_pw_correct=is_pw_correct)

    def post(self):
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
                return redirect(url_for('AuthView:get'))


class DeleteUserView(AuthViewMin):
    decorators = [login_required]
    route_prefix = '/delete'

    def post(self):
        if current_user.is_want_leave:
            user_datastore.delete_user(current_user)
            logout_user()
            user_datastore.commit()
            flash('Your account is successfully deleted!')
            return redirect(url_for('MainView:index'))
        else:
            flash('It is wrong approach!!!')
            return render_template('error/404.html')
