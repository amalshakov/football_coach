from django.shortcuts import render


def index(request):
    """Главная страница."""
    return render(request, 'teams/index.html')


def teams(request):
    """Выводит список всех команд."""
    pass


def team_detail(request):
    """Выводит информацию о выбранной команде."""
    pass


def my_team(request):
    """Выводит информацию о команде текущего пользователя."""
    pass


def players(request):
    """Выводит список всех игроков."""
    pass


def player_detail(request):
    """Выводит информацию о выбранном игроке."""
    pass


def profile(request):
    """Профиль выбранного пользователя."""
    pass
