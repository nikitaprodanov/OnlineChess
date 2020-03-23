from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from models import User
from passlib.hash import pbkdf2_sha256

class RegistrationForm(FlaskForm):
	""" Registration form """

	username = StringField('username_label', 
		validators=[InputRequired(message="Username required"), 
		Length(min=4, max=25, message="Username must be between 4 and 25 charachters")])
	password = PasswordField('password_label', 
		validators=[InputRequired(message="Password required"), 
		Length(min=4, max=25, message="Password must be between 4 and 25 charachters")])
	confirm_pswd = PasswordField('confirm_pswd_label', 
		validators=[InputRequired(message="Password confirmation required"), 
		EqualTo('password', message="Passwords must match")])
	submit_button = SubmitField('Create')

	# Custom validator for the username
	def validate_username(self, username):
		user_object = User.query.filter_by(username=username.data).first();
		if user_object:
			raise ValidationError("Username already exists. Please choose another username")


class LoginForm(FlaskForm):
	""" Login form """

	username = StringField('username_label', 
		validators=[InputRequired(message="Username required")])
	password = PasswordField('password_label', 
		validators=[InputRequired(message="Password required")])
	submit_button = SubmitField('Login')

	# Validate credentials
	def validate_password(self, password):
		user_object = User.query.filter_by(username=self.username.data).first()
		if user_object is None:
			raise ValidationError("Username or password is incorrect")
		elif not pbkdf2_sha256.verify(password.data, user_object.password):
			raise ValidationError("Username or password is incorrect")

class EnterMessageForm(FlaskForm):
	""" Enter message form """

	message = StringField('message_label', 
		validators=[InputRequired(message="Ypu have to type something")])
	submit_button = SubmitField('SEND')