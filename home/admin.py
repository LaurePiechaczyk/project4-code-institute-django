from django.contrib import admin
from .models import Noun, NounCategory, Gender

# Register your models here.
admin.site.register(Noun)
admin.site.register(NounCategory)
admin.site.register(Gender)