from flask_wtf import Form
from flask_security.forms import PasswordFormMixin


class UserLeaveForm(Form, PasswordFormMixin):
    pass
