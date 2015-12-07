from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from django.test.utils import setup_test_environment
setup_test_environment()


class Blankettests(TestCase):

    def test_main_page_loads(self):
        self.assertEqual(Client().get('/').status_code, 200)

    def test_countries_loads(self):
        self.assertEqual(Client().get(reverse('countries')).status_code, 200)

    def test_search_works(self):
        response = Client().get('/?q=KE')
        self.assertEqual(response.status_code, 200)
