from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('feminine', views.feminine, name='feminine'),
    path('masculine', views.masculine, name='masculine'),
    path('go_to_category/<category_id>', views.go_to_category, name='go_to_category'),
    path('go_to_category/<category_id>/feminine', views.categorie_feminine, name='categorie_feminine'),
    path('go_to_category/<category_id>/masculine', views.categorie_masculine, name='categorie_masculine'),
]
