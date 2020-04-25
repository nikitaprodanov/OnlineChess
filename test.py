from application import app
from flask import request, url_for
from wtform_fields import *
import unittest

class FlaskTestCase(unittest.TestCase):

	#Ensure that falsk was set up correctly
	def test_index(self):
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

if __name__ == '__main__':
	unittest.main()