from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # ALL GAMES
  path('games/', views.games_index, name='index'),
  # GAME DETAIL
  path('games/<int:game_id>/', views.games_detail, name='detail')
]