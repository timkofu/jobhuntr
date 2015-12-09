from django.test import TestCase
from django.test import Client
from django.utils.six import StringIO
from django.core.urlresolvers import reverse
from django.core.management import call_command
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

    def test_remove_expired_management_command(self):
        out = StringIO()
        call_command('remove_expired', stdout=out)
        self.assertIn("", out.getvalue())
