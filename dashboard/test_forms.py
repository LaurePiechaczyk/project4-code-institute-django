from django.test import TestCase
from .forms import ItemForm, NounForm
from home.models import Gender


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_ItemForm_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])


class TestNounForm(TestCase):

    def test_noun_german_is_required(self):
        form = NounForm({'german_noun': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('german_noun', form.errors.keys())
        self.assertEqual(
            form.errors['german_noun'][0], 
            'This field is required.'
            )

    def test_noun_gender_is_required(self):
        form = NounForm({'gender': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('gender', form.errors.keys())
        self.assertEqual(form.errors['gender'][0], 'This field is required.')

    def test_noun_english_plural_are_not_required(self):
        noun_gender_create = Gender.objects.create(noun_gender="Feminin")
        gender_pk = Gender.objects.get(noun_gender="Feminin").pk
        form = NounForm({'german_noun': 'German', 'gender': gender_pk})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_NounForm_metaclass(self):
        form = NounForm()
        self.assertEqual(form.Meta.fields, [
            'gender', 
            'german_noun', 
            'english_noun', 
            'german_plural'
            ])
