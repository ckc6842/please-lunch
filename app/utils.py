from flask import jsonify
from app.models import user_datastore, security

__author__ = 'maxto'


def _render_json(form, include_user=True, include_auth_token=False):
    has_errors = len(form.errors) > 0

    if has_errors:
        code = 400
        response = dict(errors=form.errors)
    else:
        code = 200
        response = dict()
        if include_user:
            response['user'] = dict(id=str(form.user.id))
        if include_auth_token:
            token = form.user.get_auth_token()
            response['user']['authentication_token'] = token

    return jsonify(dict(meta=dict(code=code), response=response))


def _commit(response=None):
    user_datastore.commit()
    return response


def _ctx(endpoint):
    return security._run_ctx_processor(endpoint)