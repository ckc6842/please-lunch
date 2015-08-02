# Import db
from app import db

# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug import check_password_hash

# Import the database object from the main app module

# Import module forms
from app.mod_account.forms import LoginForm, JoinForm

# Import module models (i.e. User)
from app.models import User, security

# Import flask login dependencies
from flask.ext.login import login_user, logout_user
from flask.ext.security import login_required

# Define the blueprint: 'account', set its url prefix: app.url/account
mod_account = Blueprint('account', __name__, url_prefix='/account')

"""
# Set the route and accepted methods
@mod_account.route('/login', methods=['GET', 'POST'])
def login():
    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and user.password == form.password.data:

            session['user_id'] = user.id

            flash('Welcome %s' % user.name)

            login_user(user)

            return redirect(url_for('main.index'))

        flash('Wrong email or password', 'error-message')

    return render_template("account/login.html", form=form)

@mod_account.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@security.register_context_processor
@mod_account.route('/join', methods=['GET', 'POST'])
def join():
    form = JoinForm(request.form)

    if form.validate_on_submit():
        print "POST!!"
        user = User(form.name.data, form.email.data,
                    form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('main.index'))
    print "Not Post!!"
    return render_template('account/join.html', form=form)
"""
