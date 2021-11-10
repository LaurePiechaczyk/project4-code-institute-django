from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('feminine', views.feminine, name='feminine'),
    path('masculine', views.masculine, name='masculine'),
    path('neutral', views.neutral, name='neutral'),

    path('go_to_category/<category_id>', views.go_to_category, name='go_to_category'),

    path('go_to_category/<category_id>/feminine', views.categorie_feminine, name='categorie_feminine'),
    path('go_to_category/<category_id>/masculine', views.categorie_masculine, name='categorie_masculine'),
    path('go_to_category/<category_id>/neutral', views.categorie_neutral, name='categorie_neutral'),

    path('feminineuser', views.feminine_user, name='feminine_user'),
    path('masculineuser', views.masculine_user, name='masculine_user'),
    path('neutraluser', views.neutral_user, name='neutral_user'), 
]
