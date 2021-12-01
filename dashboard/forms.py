from django import forms
from home.models import Noun, Gender, NounCategory
from .models import Item 


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']


class NounForm(forms.ModelForm):
        class Meta:
                model = Noun
                fields = [
                        'gender',
                        'german_noun',
                        'english_noun', 
                        'german_plural'
                        ]
