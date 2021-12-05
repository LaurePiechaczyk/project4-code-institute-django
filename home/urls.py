from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path(
        'go_to_category/<category_id>', 
        views.go_to_category, 
        name='go_to_category'
        ),
    path(
        'go_to_category/<category_id>/<clicked_gender>', 
        views.categorie_gender, 
        name='categorie_gender'
        ),
    path('gender/<user_or_default>/<clicked_gender>', views.user_or_default_gender, name='user_or_default_gender'),
]
