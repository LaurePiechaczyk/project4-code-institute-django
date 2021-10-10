from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include, re_path

urlpatterns = [
    path('', views.home, name='home'), 
    path('feminine', views.feminine, name='feminine'), 
    path('masculine', views.masculine, name='masculine'), 
    path('go_to_category/<category_id>', views.go_to_category, name='go_to_category'), 
    path('gender_category', views.gender_category, name='gender_category'), 
    path('go_to_category/<int>', views.ttt, name='ttt'),
]