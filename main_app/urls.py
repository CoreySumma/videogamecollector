from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # SIGN UP
  path('accounts/signup/', views.signup, name='signup'),
  # ALL GAMES
  path('games/', views.games_index, name='index'),
  # GAME DETAIL
  path('games/<int:game_id>/', views.games_detail, name='detail'),
  # CREATE NEW GAME ----> CBV(class based view)
  path('games/create/', views.GameCreate.as_view(), name='games_create'),
  # UPDATE GAME ---> CBV
  path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
  # DELETE GAME ---> CBV
  path('games/<int:pk>/delete', views.GameDelete.as_view(), name='games_delete'),
  # ASSOCIATE PLAYING (not class based)
  path('games/<int:game_id>/assoc_game/', views.assoc_game, name='assoc_game'),
  # UNASSOCIATE PLAYING (also not class based)
  path('games/<int:game_id>/unassoc_game/', views.unassoc_game, name='unassoc_game'),
  # ADD PHOTO FOR GAME
  path('games/<int:game_id>/add_photo/', views.add_photo, name='add_photo'),
]