from flask import render_template
from flask.ext.login import  login_user
from flask_social import login_failed
from flask_social.views import connect_handler
from flask_social.utils import get_connection_values_from_oauth_response
from app.models import security
from app import db, app

import random
import string


@login_failed.connect_via(app)
def on_login_failed(sender, provider, oauth_response):
    print "good"
    connection_values = get_connection_values_from_oauth_response(provider, oauth_response)
    ds = security.datastore
    user = ds.create_user(email='test999@fox.net', password=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20)))
    ds.commit()
    connection_values['user_id'] = user.id
    connect_handler(connection_values, provider)
    login_user(user)
    db.session.commit()
    return render_template('main/index.html')