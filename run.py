# -*- coding: utf-8 -*-

__author__ = 'maxto'
# Run a test server.
from app import app, db
from flask import render_template
from flask.ext.login import login_user
from flask_security.utils import encrypt_password
from flask_social import login_failed
from flask_social.views import connect_handler
from flask_social.utils import get_connection_values_from_oauth_response
from app.models import security
import string
import random
import hashlib
import re

# When connection table hasn't user's facebook information.
# Automatically login.
@login_failed.connect_via(app)
def on_login_failed(sender, provider, oauth_response):
    hashlib.digest_size = 10
    connection_values = get_connection_values_from_oauth_response(provider, oauth_response)
    at = hashlib.md5()
    at.update(connection_values['access_token'])
    email = at.hexdigest()+'@fox.net'
    password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))

    ds = security.datastore
    user = ds.create_user(email=email, password=encrypt_password(password))
    ds.commit()
    connection_values['user_id'] = user.id
    connect_handler(connection_values, provider)
    login_user(user)
    db.session.commit()

    return render_template('main/index.html')


@app.template_filter('quoted')
def quoted(s):
    l = re.findall('\'([^\']*)\'', str(s))
    if l:
        return l[0]
    return None

# 'app.run' is different by os.
import sys

if sys.platform == 'win32':
    app.run(host='127.0.0.1', port=8080, debug=True)
elif sys.platform == 'linux2':
    app.run(host='0.0.0.0', port=8080, debug=True)
else:
    app.run(host='127.0.0.1', port=8080, debug=True)


