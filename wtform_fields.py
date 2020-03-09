from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
	""" Registration form """

	username = StringField('username_label')
	password = PasswordField('password_label')
	confirm_pswd = PasswordField('confirm_pswd_label')