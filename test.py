from application import app
from flask import request, url_for
from wtform_fields import *
import unittest

class FlaskTestCase(unittest.TestCase):

	""" LOGIN SECTION """

	#Ensure that falsk was set up correctly
	def test_login(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	#Ensure that login page loads correctly
	def test_login_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertTrue(b'Login' in response.data)

	#Ensure that login page responds correctly to correct credentials
	def test_login_correct_credentials(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data={
				'username': 'User3',
				'password': 'test'
			},
			follow_redirects=True
		)
		assert response.status == '200 OK'

	#Ensure that login page behaves correctly on unexisting credentials
	def test_login_unexisting_credentials(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data={
				'username': 'a',
				'password': 'a'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username or password is incorrect', response.data)

	#Ensure that login page behaves correctly on unexisting username but existing password
	def test_login_unexisting_username_credentials(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data={
				'username': 'jojo',
				'password': 'test'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username or password is incorrect', response.data)

	#Ensure that login page behaves correctly on unverifyed password
	def test_login_unverifyed_password_credentials(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data={
				'username': 'User3',
				'password': 'test1'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username or password is incorrect', response.data)

	# #Ensure that logout works correctly
	def test_logout_redirect(self):
		tester = app.test_client(self)
		response = tester.get('/logut', follow_redirects=True)
		self.assertEqual(response.status_code, 404)


	"""REGISTER SECTION"""

	#Ensure that register page was set up correctly
	def test_register(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	#Ensure that register page loads up correctly
	def test_register_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type='html/text')
		self.assertTrue(b'Get started' in response.data)

	"""Username Validation"""

	#Ensure that register page returns the correct response when the username is too short
	def test_register_short_username(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'a',
				'password': 'test',
				'confirm_pswd': 'test'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username must be between 4 and 25 charachters', response.data)

	#Ensure that register page returns the correct response when the username is too large
	def test_register_long_username(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'qwertyuiopasdfghjklzxcvbnm',
				'password': 'test',
				'confirm_pswd': 'test'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username must be between 4 and 25 charachters', response.data)

	#Ensure that register page returns the correct response when the username has valid length
	def test_register_valid_username(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'jojo',
				'password': 'test',
				'confirm_pswd': 'test'
			},
			follow_redirects=True
		)
		assert response.status == '200 OK'

	#Ensure that register page returns the correct response when the username is already taken
	def test_register_taken_username(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'User3',
				'password': 'test',
				'confirm_pswd': 'test'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username already exists. Please choose another username', response.data)

	"""Password Validation"""

	#Ensure that register page returns the correct response when the password is too short
	def test_register_short_password(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'jojo',
				'password': 'a',
				'confirm_pswd': 'a'
			},
			follow_redirects=True
		)
		self.assertIn(b'Password must be between 4 and 25 charachters', response.data)

	#Ensure that register page returns the correct response when the password is too large
	def test_register_long_password(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'jojo',
				'password': 'qwertyuiopasdfghjklzxcvbnm',
				'confirm_pswd': 'qwertyuiopasdfghjklzxcvbnm'
			},
			follow_redirects=True
		)
		self.assertIn(b'Password must be between 4 and 25 charachters', response.data)

	#Ensure that register page returns the correct response when the password has valid length
	def test_register_valid_password(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'jojo',
				'password': 'test',
				'confirm_pswd': 'test'
			},
			follow_redirects=True
		)
		assert response.status == '200 OK'

	"""Confirm Password Validation"""

	#Ensure that register page returns the correct response when the confirm password does not match the given password
	def test_register_confirm_pswd_not_match(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'jojo',
				'password': 'test1',
				'confirm_pswd': 'test2'
			},
			follow_redirects=True
		)
		self.assertIn(b'Passwords must match', response.data)

	#Ensure that register page returns the correct response when the password and the confirm password field match
	def test_register_confirm_pswd_match(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'jojo',
				'password': 'test1',
				'confirm_pswd': 'test1'
			},
			follow_redirects=True
		)
		assert response.status == '200 OK'

	"""Combined Validation Errors"""

	#Ensure that register page returns the correct response when the username and password are short
	def test_register_short_credentials(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'j',
				'password': 't',
				'confirm_pswd': 't'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username must be between 4 and 25 charachters', response.data)
		self.assertIn(b'Password must be between 4 and 25 charachters', response.data)

	#Ensure that register page returns the correct response when the username and password are long
	def test_register_long_credentials(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'qwertyuiopasdfghjklzxcvbnm',
				'password': 'qwertyuiopasdfghjklzxcvbnm',
				'confirm_pswd': 'qwertyuiopasdfghjklzxcvbnm'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username must be between 4 and 25 charachters', response.data)
		self.assertIn(b'Password must be between 4 and 25 charachters', response.data)

	#Ensure that register page returns the correct response when the password is short and doesn't match the confirm password
	def test_register_short_password_not_matching(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'jojo',
				'password': 't1',
				'confirm_pswd': 't2'
			},
			follow_redirects=True
		)
		self.assertIn(b'Password must be between 4 and 25 charachters', response.data)
		self.assertIn(b'Passwords must match', response.data)

	#Ensure that register page returns the correct response when the password is long and doesn't match the confirm password
	def test_register_long_password_not_matching(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'jojo',
				'password': 'qwertyuiopasdfghjklzxcvbnm1',
				'confirm_pswd': 'qwertyuiopasdfghjklzxcvbnm2'
			},
			follow_redirects=True
		)
		self.assertIn(b'Password must be between 4 and 25 charachters', response.data)
		self.assertIn(b'Passwords must match', response.data)

	#Ensure that register page returns the correct response when the username is short and doesn't match the confirm password
	def test_register_short_username_not_matching(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'j',
				'password': 'test1',
				'confirm_pswd': 'test2'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username must be between 4 and 25 charachters', response.data)
		self.assertIn(b'Passwords must match', response.data)

	#Ensure that register page returns the correct response when the username is long and doesn't match the confirm password
	def test_register_long_username_not_matching(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'qwertyuiopasdfghjklzxcvbnm',
				'password': 'test1',
				'confirm_pswd': 'test2'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username must be between 4 and 25 charachters', response.data)
		self.assertIn(b'Passwords must match', response.data)

	#Ensure that register page returns the correct response when the username and password are short and don't match
	def test_register_short_username_short_password_not_matching(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'j',
				'password': 't1',
				'confirm_pswd': 't2'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username must be between 4 and 25 charachters', response.data)
		self.assertIn(b'Password must be between 4 and 25 charachters', response.data)
		self.assertIn(b'Passwords must match', response.data)

	#Ensure that register page returns the correct response when the username and password are long and don't match
	def test_register_long_username_long_password_not_matching(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'qwertyuiopasdfghjklzxcvbnm',
				'password': 'qwertyuiopasdfghjklzxcvbnm1',
				'confirm_pswd': 'qwertyuiopasdfghjklzxcvbnm2'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username must be between 4 and 25 charachters', response.data)
		self.assertIn(b'Password must be between 4 and 25 charachters', response.data)
		self.assertIn(b'Passwords must match', response.data)

	#Ensure that register page returns the correct response when the username is short and password is long and don't match
	def test_register_short_username_long_password_not_matching(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'j',
				'password': 'qwertyuiopasdfghjklzxcvbnm1',
				'confirm_pswd': 'qwertyuiopasdfghjklzxcvbnm2'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username must be between 4 and 25 charachters', response.data)
		self.assertIn(b'Password must be between 4 and 25 charachters', response.data)
		self.assertIn(b'Passwords must match', response.data)

	#Ensure that register page returns the correct response when the username is long and password is short and don't match
	def test_register_long_username_short_password_not_matching(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'qwertyuiopasdfghjklzxcvbnm',
				'password': 't1',
				'confirm_pswd': 't2'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username must be between 4 and 25 charachters', response.data)
		self.assertIn(b'Password must be between 4 and 25 charachters', response.data)
		self.assertIn(b'Passwords must match', response.data)

	#Ensure that register page returns the correct response when the username is taken and password is short
	def test_register_taken_short_credentials(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'User3',
				'password': 't',
				'confirm_pswd': 't'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username already exists. Please choose another username', response.data)
		self.assertIn(b'Password must be between 4 and 25 charachters', response.data)

	#Ensure that register page returns the correct response when the username is taken and password is long
	def test_register_taken_long_credentials(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'User3',
				'password': 'qwertyuiopasdfghjklzxcvbnm',
				'confirm_pswd': 'qwertyuiopasdfghjklzxcvbnm'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username already exists. Please choose another username', response.data)
		self.assertIn(b'Password must be between 4 and 25 charachters', response.data)

	#Ensure that register page returns the correct response when the username is taken and doesn't match the confirm password
	def test_register_taken_username_not_matching(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'User3',
				'password': 'test1',
				'confirm_pswd': 'test2'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username already exists. Please choose another username', response.data)
		self.assertIn(b'Passwords must match', response.data)

	#Ensure that register page returns the correct response when the username is taken and password is short and don't match
	def test_register_taken_username_short_password_not_matching(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'User3',
				'password': 't1',
				'confirm_pswd': 't2'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username already exists. Please choose another username', response.data)
		self.assertIn(b'Password must be between 4 and 25 charachters', response.data)
		self.assertIn(b'Passwords must match', response.data)

	#Ensure that register page returns the correct response when the username is taken and password is long and don't match
	def test_register_taken_username_long_password_not_matching(self):
		tester = app.test_client(self)
		response = tester.post(
			'/',
			data={
				'username': 'User3',
				'password': 'qwertyuiopasdfghjklzxcvbnm1',
				'confirm_pswd': 'qwertyuiopasdfghjklzxcvbnm2'
			},
			follow_redirects=True
		)
		self.assertIn(b'Username already exists. Please choose another username', response.data)
		self.assertIn(b'Password must be between 4 and 25 charachters', response.data)
		self.assertIn(b'Passwords must match', response.data)

	"""UNAUTHORITIZED SECTION"""

	#Ensure that edit page is not available when no user has logged in
	def test_edit_unauthoritized(self):
		tester = app.test_client(self)
		response = tester.get('/edit', follow_redirects=True)
		self.assertEqual(response.status_code, 401)

	#Ensure that lobby page is not available when no user has logged in
	def test_lobby_unauthoritized(self):
		tester = app.test_client(self)
		response = tester.get('/lobby', follow_redirects=True)
		self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
	unittest.main()