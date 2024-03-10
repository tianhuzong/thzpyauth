from django.test import TestCase,Client
from django.urls import reverse
import utils.string
# Create your tests here.

class PublicTest(TestCase):
    def setUp(self):
        self.client = Client()
    def test_Service_state(self):
        response = self.client.get(reverse("api:service_state"))
        self.assertEqual(response.status_code,200)
        self.assertTrue(utils.string.ipv4(response.json().get("data").get("ip")))