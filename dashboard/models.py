from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
        )

    def __str__(self):
        return self.name
        