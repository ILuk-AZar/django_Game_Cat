from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('add/', views.add_game, name='add_game'),
    path('delete/<int:game_id>/', views.delete_game, name='delete_game'),
]