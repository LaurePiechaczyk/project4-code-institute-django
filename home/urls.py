from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<clicked_gender>', views.gender, name='gender'),
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
    path('user/<clicked_gender>', views.user_gender, name='user_gender'),
]
