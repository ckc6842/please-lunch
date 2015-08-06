from flask import render_template, redirect, request, current_app, session, \
    flash, url_for, Blueprint
from flask.ext.security import LoginForm, current_user, login_required, \
    login_user
from flask.ext.social.utils import get_provider_or_404


mod_auth = Blueprint('auth', __name__, url_prefix='/auth')


@mod_auth.route('/register', methods=['GET', 'POST'])
@mod_auth.route('/register/<provider_id>', methods=['GET', 'POST'])
def register(provider_id=None):
    if current_user.is_authenticated():
        return redirect(request.referrer or '/')

    if provider_id:
        provider = get_provider_or_404(provider_id)
        connection_values = session.get('failed_login_connection', None)
    else:
        provider = None
        connection_values = None

    login_failed = int(request.args.get('login_failed', 0))

    return render_template('security/register_user.html',
                           provider=provider,
                           login_failed=login_failed,
                           connection_values=connection_values)