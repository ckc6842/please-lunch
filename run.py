__author__ = 'maxto'
# Run a test server.
from app import app, db
from flask import render_template
from flask.ext.login import  login_user
from flask_security.utils import encrypt_password
from flask_social import login_failed
from flask_social.views import connect_handler
from flask_social.utils import get_connection_values_from_oauth_response
from app.models import security
import string
import random


# When connection table hasn't user's facebook information.
# Automatically login.
@login_failed.connect_via(app)
def on_login_failed(sender, provider, oauth_response):
    connection_values = get_connection_values_from_oauth_response(provider, oauth_response)
    ds = security.datastore
    user = ds.create_user(email=connection_values['full_name']+'@fox.net',
                          password=encrypt_password(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))))
    ds.commit()
    connection_values['user_id'] = user.id
    connect_handler(connection_values, provider)
    login_user(user)
    db.session.commit()

    return render_template('main/index.html')

# 'app.run' is different by os.
import sys

if sys.platform == 'win32':
    app.run(host='127.0.0.1', port=80, debug=True)
elif sys.platform == 'linux2':
    app.run(host='0.0.0.0', port=8080, debug=True)
else:
    app.run(host='127.0.0.1', port=8080, debug=True)


