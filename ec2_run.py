# Run a test server.
from app import app, db
from flask import current_app, render_template
from flask.ext.login import  login_user
from flask_social import login_failed
from flask_social.views import connect_handler
from flask_social.utils import get_connection_values_from_oauth_response

# for ec2 instance testing.
app.run(host='0.0.0.0', port=8080, debug=True)


@login_failed.connect_via(app)
def on_login_failed(sender, provider, oauth_response):
    print "good"
    connection_values = get_connection_values_from_oauth_response(provider, oauth_response)
    ds = current_app.security.datastore
    user = ds.create_user(email='test999@fox.net', password='123456') #fill in relevant stuff here
    ds.commit()
    connection_values['user_id'] = user.id
    connect_handler(connection_values, provider)
    login_user(user)
    db.commit()
    return render_template('main/index.html')
