# game/urls


from django.urls import path
from game import views

urlpatterns = [
    path("", views.start_game, name='start_game'),
    path("game/", views.play_game, name='play_game'),
    path("result/<str:player_choice>/<str:computer_choice>/", views.game_result, name='game_result'),
    path("end/", views.end_game, name='end_game')
]
