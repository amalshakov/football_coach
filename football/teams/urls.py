from django.urls import path

from . import views

app_name = 'teams'

urlpatterns = [
    path('', views.index, name='index'),
    path('teams/', views.teams, name='teams_list'),
    path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
    path('my_team/', views.my_team, name='my_team'),
    path('players/', views.players, name='players_list'),
    path('players/<int:player_id>/', views.player_detail, name='player_detail'),
    path('profile/<str:username>/', views.profile, name='profile'),
]
