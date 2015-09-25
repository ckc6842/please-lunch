from flask_wtf import Form
from flask_security.forms import PasswordFormMixin, RegisterForm


class UserLeaveForm(Form, PasswordFormMixin):
    pass


class ExtendedRegisterForm(RegisterForm):
    pass
