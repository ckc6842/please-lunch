# Run a test server.
from app import app, db
from flask import render_template
from flask.ext.login import  login_user
from flask_security.utils import encrypt_password
from flask_social import login_failed
from flask_social.views import connect_handler
from flask_social.utils import get_connection_values_from_oauth_response
from app.models import security

import random
import string

# for ec2 instance testing.
app.run(host='0.0.0.0', port=8080, debug=True)

@login_failed.connect_via(app)
def on_login_failed(sender, provider, oauth_response):
    connection_values = get_connection_values_from_oauth_response(provider, oauth_response)
    ds = security.datastore
    print '_______'+connection_values+'__________'
    user = ds.create_user(email=''.join(random.choice(string.ascii_uppercase + string.digits)
                                        for _ in range(5))+'@fox.net',
                          password=encrypt_password('123456'))
    ds.commit()
    connection_values['user_id'] = user.id
    connect_handler(connection_values, provider)
    login_user(user)
    db.session.commit()
    return render_template('main/index.html')