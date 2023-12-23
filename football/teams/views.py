from django.shortcuts import render

from .models import Player, Team


def index(request):
    """Главная страница."""
    return render(request, 'teams/index.html')


def teams(request):
    """Выводит список всех команд."""
    teams = Team.objects.all()
    context = {
        'teams': teams,
    }
    return render(request, 'teams/teams_list.html', context)


def team_detail(request):
    """Выводит информацию о выбранной команде."""
    pass


def my_team(request):
    """Выводит информацию о команде текущего пользователя."""
    pass


def players(request):
    """Выводит список всех игроков."""
    players = Player.objects.all()
    context = {
        'players': players,
    }
    return render(request, 'teams/players_list.html', context)


def player_detail(request):
    """Выводит информацию о выбранном игроке."""
    pass


def profile(request):
    """Профиль выбранного пользователя."""
    pass
