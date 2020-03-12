from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, current_user

from wtform_fields import *
from models import *

# Configure app
app = Flask(__name__)
app.secret_key = 'replace later'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI']='postgres://kcszumbnyngcpe:b6bff3fa03331de5fa50e583ab82b05524c0e1b1551fdc98673a56c558fbff29@ec2-35-168-54-239.compute-1.amazonaws.com:5432/d8ru7iuptl4q1i'
db = SQLAlchemy(app)

# Configure login manager
login = LoginManager()
login.init_app(app)

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
		return redirect(url_for('login'))

	return render_template("index.html", form=reg_form)

# Login route
@app.route("/login", methods=['GET', 'POST'])
def login():

	login_form = LoginForm()

	if login_form.validate_on_submit():
		user_object = User.query.filter_by(username=login_form.username.data).first()
		login_user(user_object)
		if current_user.is_authenticated:
			return "Logged in with flask login"

		return "Not logged in"

	return render_template("login.html", form=login_form)

if __name__ == "__main__":
	app.run(debug=True)