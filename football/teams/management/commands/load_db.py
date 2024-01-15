import json
import os

from django.conf import settings
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from teams.models import Team, Player

User = get_user_model()


def process_file(name: str):
    with open(
        os.path.join(settings.BASE_DIR, 'static/data/', name),
        'r',
        encoding='utf-8'
    ) as file:
        return json.load(file)


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Загружаем Players.
        data = process_file('players.json')
        for name, value in data.items():
            Player.objects.get_or_create(
                name=name,
                age=value[0],
                power=value[1],
                position=value[2],
                country=value[3]
            )
        print('----- Players is LOAD -----')

        # Загружаем Teams.
        data = process_file('teams.json')
        for name, value in data.items():
            team, created = Team.objects.get_or_create(
                name=name,
                city=value[0],
                stadium=value[1]
            )
            if created:
                with open(f'static/data/emblem/{name}.png', 'rb') as file:
                    image = ImageFile(file)
                    team.emblem.save(f'{name}.png', image)
        print('----- Teams is LOAD -----')

        # Загружаем Users.
        # data = process_file('users.json')
        # for username, value in data.items():
        #     User.objects.get_or_create(
        #         username=username,
        #         password=value[0],
        #         first_name=value[1],
        #         last_name=value[2],
        #         email=[3]
        #     )
        # print('----- Users is LOAD -----')
