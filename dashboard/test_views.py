from django.test import TestCase
from .models import Item


class TestViews(TestCase):

    def test_dashboard_not_accessible_for_not_login(self):
        response = self.client.get('dashboard/')
        self.assertEqual(response.status_code, 404)
