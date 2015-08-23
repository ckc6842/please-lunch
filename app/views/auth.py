# -*- coding: utf-8 -*-
__author__ = 'maxto'

from flask import render_template, redirect, url_for, flash
from flask_classy import FlaskView
from flask.ext.login import login_required, current_user, logout_user
from flask_security.utils import verify_and_update_password

from app.models import user_datastore
from app.forms import UserLeaveForm
from app import db

class AuthViewMin(FlaskView):
    route_base = '/auth/'
    decorators = [login_required]


class AuthView(AuthViewMin):
    def profile(self):
        return render_template('main/profile.html')


class LeaveView(AuthViewMin):
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