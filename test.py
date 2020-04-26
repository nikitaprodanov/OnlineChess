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

	#Ensure that login page behaves correctly on wrong credentials
	def test_login_wrong_credentials(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
			data={
				'username': 'a',
				'password': 'a'
			},
			follow_redirects=True
		)
		self.assertIn(b'incorrect', response.data)

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

if __name__ == '__main__':
	unittest.main()