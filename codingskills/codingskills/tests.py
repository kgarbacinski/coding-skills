from django.test import TestCase, Client

'''
Test URLs
'''

class TestMainURL(TestCase):
    URL = '/'

    def setUp(self):
        self.client = Client()

    def test_should_return_redirect_when_main_route_is_loaded(self) -> None:
        response = self.client.get(TestMainURL.URL)

        self.assertEqual(response.status_code, 200)

class TestAdminURL(TestCase):
    URL = '/palindrome'

    def setUp(self):
        self.client = Client()

    def test_should_return_redirect_when_admin_url_is_loaded(self) -> None:
        response = self.client.get(TestAdminURL.URL)

        self.assertEqual(response.status_code, 301)