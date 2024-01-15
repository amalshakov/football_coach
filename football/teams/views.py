from django.shortcuts import get_object_or_404, redirect, render

from .models import Player, Team
from .forms import TakeControlForm


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


def team_detail(request, team_id):
    """Выводит информацию о выбранной команде."""
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        form = TakeControlForm(request.POST)
        if form.is_valid():
            team.coach = request.user
            team.save()
            return redirect('teams:players_list')
    else:
        form = TakeControlForm(initial={'team_id': team_id})
    context = {
        'team': team,
        'form': form,
    }
    return render(request, 'teams/team_detail.html', context)


def my_team(request):
    """Выводит информацию о команде текущего пользователя."""
    team = request.user.team
    context = {
        'team': team,
    }
    return render(request, 'teams/my_team.html', context)


def players(request):
    """Выводит список всех игроков.
    Можно передавать доп параметр sort_param
    для сортировки игроков.
    """
    sort_param = request.GET.get('sort')
    if sort_param and sort_param in ['calculate_cost', '-calculate_cost']:
        players = Player.objects.all()
        if sort_param[0] != '-':
            players = sorted(players, key=lambda x: x.calculate_cost(), reverse=True)
            flag = True
        else:
            players = sorted(players, key=lambda x: x.calculate_cost())
            flag = False
    elif sort_param:
        players = Player.objects.order_by(sort_param)
        if sort_param[0] != '-':
            flag = True
        else:
            flag = False
    else:
        players = Player.objects.all()
        flag = False
    context = {
        'players': players,
        'flag': flag,
    }
    return render(request, 'teams/players_list.html', context)


def player_detail(request):
    """Выводит информацию о выбранном игроке."""
    pass


def profile(request):
    """Профиль выбранного пользователя."""
    pass
