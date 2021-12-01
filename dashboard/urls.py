from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'), 

    path('dashboard/todo', views.todo_dashboard, name='todo_dashboard'), 
    path('dashboard/add_todo_item', views.add_todo_item, name='add_todo_item'), 
    path(
        'dashboard/edit_todo_item/<item_id>', 
        views.edit_todo_item, 
        name='edit_todo_item'
        ), 
    path(
        'dashboard/toggle_todo_item/<item_id>', 
        views.toggle_todo_item, 
        name='toggle_todo_item'
        ), 
    path(
        'dashboard/delete_todo_item/<item_id>', 
        views.delete_todo_item, 
        name='delete_todo_item'
        ), 

    path('dashboard/nouns', views.noun_dashboard, name='noun_dashboard'), 
    path('dashboard/add_noun', views.add_noun, name='add_noun'), 
    path('dashboard/edit_noun/<noun_id>', views.edit_noun, name='edit_noun'), 
    path(
        'dashboard/delete_noun/<noun_id>', 
        views.delete_noun, 
        name='delete_noun'
        ), 
]
