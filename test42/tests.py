from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):

	def test_view_status(self):
		response = self.client.get('')
		self.assertEqual(response.status_code, 200)
