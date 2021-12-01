from django.test import TestCase
from home.models import NounCategory


class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_feminin_page(self):
        response = self.client.get('/feminine')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_masculin_page(self):
        response = self.client.get('/masculine')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_neutral_page(self):
        response = self.client.get('/neutral')
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

    def test_go_to_category_feminine_page(self):
        category_created = NounCategory.objects.create(
            noun_category="CategoryTest"
            )
        category_pk = NounCategory.objects.get(noun_category="CategoryTest").pk
        response = self.client.get(f'/go_to_category/{category_pk}/feminine')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_go_to_category_masculine_page(self):
        category_created = NounCategory.objects.create(
            noun_category="CategoryTest"
            )
        category_pk = NounCategory.objects.get(noun_category="CategoryTest").pk
        response = self.client.get(f'/go_to_category/{category_pk}/masculine')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_go_to_category_neutral_page(self):
        category_created = NounCategory.objects.create(
            noun_category="CategoryTest"
            )
        category_pk = NounCategory.objects.get(noun_category="CategoryTest").pk
        response = self.client.get(f'/go_to_category/{category_pk}/neutral')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        