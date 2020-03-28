from time import localtime, strftime

from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

from flask_socketio import SocketIO, send, emit, join_room, leave_room

from wtform_fields import *
from models import *
from datetime import datetime
import logging

# Configure app
app = Flask(__name__)
app.secret_key = 'replace later'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI']='postgres://kcszumbnyngcpe:b6bff3fa03331de5fa50e583ab82b05524c0e1b1551fdc98673a56c558fbff29@ec2-35-168-54-239.compute-1.amazonaws.com:5432/d8ru7iuptl4q1i'
db = SQLAlchemy(app)

# Initialize Flask-SocketIO
socketio = SocketIO(app)

 # Predefined rooms
ROOMS = ["lobby", "news", "rules"]

# Configure login manager
login = LoginManager()
login.init_app(app)

# Logging configuration
logging.basicConfig(filename = 'logs.log', level=logging.DEBUG)
app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True

def i_logger(text):
	time_now = datetime.now()
	date = time_now.strftime("%D %T ")
	logging.info(date + text)

def w_logger(text):
	time_now = datetime.now()
	date = time_now.strftime("%D %T ")
	logging.warning(date + text)

def e_logger(text):
	time_now = datetime.now()
	date = time_now.strftime("%D %T ")
	logging.error(date + text)

@login.user_loader
def load_user(id):

	return User.query.get(int(id))


# Registration route
@app.route("/", methods=['GET', 'POST'])
def index():

	reg_form = RegistrationForm()
	if reg_form.validate_on_submit():
		username = reg_form.username.data
		password = reg_form.password.data

		# Hashing the password
		hashed_pswd = pbkdf2_sha256.hash(password)

		# If no such username add the user to the database
		user = User(username=username, password=hashed_pswd)
		db.session.add(user)
		db.session.commit()
		text = 'new account made with username: ' + str(username) + '.' 
		return redirect(url_for('login'))

	return render_template("index.html", form=reg_form)

# Login route
@app.route("/login", methods=['GET', 'POST'])
def login():

	login_form = LoginForm()

	if login_form.validate_on_submit():
		user_object = User.query.filter_by(username=login_form.username.data).first()
		login_user(user_object)
		text = 'user: ' + str(current_user.username) + ' with id:' + str(current_user.id) + ' logged in.'
		i_logger(text)
		return redirect(url_for('lobby'))
	text = "failed attempt to login."
	w_logger(text)
	return render_template("login.html", form=login_form)


# Route for lobby ONLY for logged in users
@app.route("/lobby", methods=['GET', 'POST'])
# @login_required
def lobby():
	send_form = EnterMessageForm()

	return render_template('lobby.html', form=send_form, username=current_user.username, rooms=ROOMS)

# Logging out a user
@app.route("/logout", methods=['GET'])
def logout():
	text = " user: " + str(current_user.username) + ' with id:' + str(current_user.id) + ' logged out.'
	i_logger(text)
	logout_user()
	return "Logged out using flask login"

# Event handler
@socketio.on('message')
def message(data):
	text = ' Website accessed.'
	w_logger(text)
	# print(f"\n\n{data}\n\n")
	send({'msg': data['msg'], 'username': data['username'], 'time_stamp': strftime('%b-%d %I:%M%p', localtime())}, room=data['room'])
	# emit('some-event', 'this is a custom event message')

 # Joining a room
@socketio.on('join')
def join(data):
	text = " user: " + str(current_user.username) + ' with id:' + str(current_user.id) + ' joined a room.'
	i_logger(text)
	join_room(data['room'])
	send({'msg': data['username'] + " has joined the " + data['room'] + " room."}, room=data['room'])

 # Leaving a room
@socketio.on('leave')
def leave(data):
	text = " user: " + str(current_user.username) + ' with id:' + str(current_user.id) + ' left the room.'
	i_logger(text)
	leave_room(data['room'])
	send({'msg': data['username'] + " has left the " + data['room'] + " room."}, room=data['room'])

if __name__ == "__main__":
	socketio.run(app, debug=True)