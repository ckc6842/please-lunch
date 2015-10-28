from flask_wtf import Form
from flask_security.forms import PasswordFormMixin, RegisterForm, SubmitField, get_form_field_label


class UserLeaveForm(Form, PasswordFormMixin):
    submit = SubmitField(get_form_field_label('leave'))
    pass


class ExtendedRegisterForm(RegisterForm):
    pass
