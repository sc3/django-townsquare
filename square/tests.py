from django.test import TestCase
from django.test.client import Client
from square.models import Volunteer
from django.contrib.auth.models import User

class Test_Volunteer_URLs(TestCase):

	def test_volunteer_login_up(self):
		self.client = Client()
		response = self.client.get('/townsquare/login')
		self.assertEqual(response.status_code, 200)

	def test_volunteer_add_redirects_if_not_logged_in(self):
		response = self.client.get('/townsquare/volunteer/add', follow=True)
		self.assertEqual(response.request['PATH_INFO'], '/townsquare/login')

	def test_volunteer_add_fails_if_user_not_staff(self):
		u1 = User.objects.create_user(first_name="alan", last_name="watts", 
										username="awatts", password="secret")
		v1 = Volunteer(user=u1)
		u1.save()
		v1.save()
		self.client.login(username='awatts', password="secret")
		response = self.client.get('/townsquare/volunteer/add', follow=True)
		self.assertEqual(response.status_code, 401)