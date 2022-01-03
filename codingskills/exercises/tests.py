from django.test import TestCase, Client

class TestHomeView(TestCase):
    HOME_URL = '/'

    def setUp(self):
        self.client = Client()

    def test_should_return_200_when_app_is_running(self):
        response = self.client.get(TestHomeView.HOME_URL)

        self.assertEqual(response.status_code, 200)