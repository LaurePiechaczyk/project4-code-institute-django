from django.test import TestCase
from home.models import NounCategory


class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')


    def test_go_to_category_page(self):
        category_created = NounCategory.objects.create(
            noun_category="CategoryTest"
            )
        category_pk = NounCategory.objects.get(noun_category="CategoryTest").pk
        response = self.client.get(f'/go_to_category/{category_pk}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
