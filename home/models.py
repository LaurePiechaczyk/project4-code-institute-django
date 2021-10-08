from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class NounCategory(models.Model):
    noun_category = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.noun_category


class Gender(models.Model):
    noun_gender = models.CharField(max_length=30)

    def __str__(self):
        return self.noun_gender


class Noun(models.Model):

    german_noun = models.CharField(max_length=50, null=False, blank=False)
    # article = models.CharField(max_length=3, blank=True, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    english_noun = models.CharField(max_length=50, blank=True, null=True)
    german_plural = models.CharField(max_length=50, blank=True, null=True)
    categories = models.ManyToManyField(NounCategory, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.german_noun


class GenderToDisplay (models.Model):
    gender_to_display = models.ForeignKey(Gender, on_delete=models.CASCADE)


class ChosenCategories(models.Model):
    chosen_category = models.CharField(max_length=50, blank=True, null=True)