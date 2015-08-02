# Import Form and RecaptchaField (optional)
from flask.ext.wtf import Form # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import BooleanField, TextField, PasswordField # BooleanField

# Import Form validators
from wtforms.validators import Required, Email, EqualTo, Length

# Define the login form (WTForms)

class LoginForm(Form):
    email    = TextField('Email Address', [Email(),
                Required(message='Forgot your email address?')])
    password = PasswordField('Password', [
                Required(message='Must provide a password. ;-)')])

class JoinForm(Form):
    name = TextField('Name', [Length(min=4, max=25)])
    email = TextField('Email Address', [Length(min=6, max=35)])
    password = PasswordField('Password', [
        Required(),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [Required()])
