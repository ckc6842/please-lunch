from flask import render_template, redirect, url_for, flash
from flask_classy import FlaskView
from flask_security import login_required, current_user
from app import db


class StartView(FlaskView):
    decorators = [login_required]
    route_base = '/start'

    def index(self):
        if current_user.is_evaluate:
            return redirect(url_for('MainView:recommend'))
        else:
            return render_template('start/index.html')

    def info(self):
        if not current_user.is_evaluate:
            current_user.is_evaluate = True
            db.session.commit()
        else:
            flash('You are already evaluated')
            return redirect(url_for('MainView:recommend'))

        return redirect(url_for('StartView:evaluate'))

    def evaluate(self):
        flash('Your information successfully evaluated!')
        return redirect(url_for('MainView:recommend'))