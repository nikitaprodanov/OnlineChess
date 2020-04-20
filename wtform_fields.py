from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from models import User
from passlib.hash import pbkdf2_sha256
from flask_login import current_user
from wtforms.widgets import TextArea

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
		validators=[InputRequired(message="You have to type something")],
		widget=TextArea())
	submit_button = SubmitField('SEND')

class EditUsernameForm(FlaskForm):
	""" Edit username form """

	cur_username = StringField('cur_username_label',
		validators=[InputRequired(message="Current username required")])
	new_username = StringField('new_username_label',
		validators=[InputRequired(message="New username required"),
		Length(min=4, max=25, message="New username must be between 4 and 25 charachters")])
	submit_button = SubmitField('Edit')

	# Check if current username is real
	def validate_cur_username(self, cur_username):
		if not(current_user.username == cur_username.data):
			raise ValidationError("Please enter your current username")

	# Check if new username isn`t taken
	def validate_new_username(self, new_username):
		user_object = User.query.filter_by(username=new_username.data).first()
		if user_object:
			raise ValidationError("This username is already taken. Please try another one")