# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, session, redirect, url_for

# Import password / encryption helper tools

# Import the database object from the main app module

# Import module forms
from app.mod_account.forms import LoginForm

# Import module models (i.e. User)
from app.models import User

# Import database
from app import db, app

# Import flask login dependencies
from flask.ext.login import login_required, user_logged_in, LoginManager, UserMixin, current_user, login_user, logout_user
from flask.ext.security import AnonymousUser

# Define the blueprint: 'account', set its url prefix: app.url/account
mod_account = Blueprint('account', __name__, url_prefix='/account')

# flask-login setting
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.anonymous_user = AnonymousUser

# Set the route and accepted methods
@mod_account.route('/login/', methods=['GET', 'POST'])
def signin():

    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and user.password == form.password.data:

            session['user_id'] = user.id

            flash('Welcome %s' % user.name)

            login_user(user)

            return redirect(url_for('main'))

        flash('Wrong email or password', 'error-message')

    return render_template("account/signin.html", form=form)
