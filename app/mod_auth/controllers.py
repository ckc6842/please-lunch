# -*- coding: utf-8 -*-
__author__ = 'maxto'

from flask import Blueprint, render_template, redirect, url_for, flash
from flask.ext.login import login_required, current_user, logout_user
from app.models import user_datastore
from forms import UserLeaveForm
from app import db
from flask_security.utils import verify_and_update_password

# 페이스북 연동용 ... 잘 안 됨.

mod_auth = Blueprint('auth', __name__, url_prefix='')


@mod_auth.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    return render_template('main/profile.html')


@mod_auth.route('/leave', methods=['POST', 'GET'])
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


@mod_auth.route('/delete', methods=['POST', 'GET'])
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

