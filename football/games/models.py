from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

from teams.models import Player

User = get_user_model()


class Game(models.Model):
    '''Игра, информация об игре.'''
    FORMATION_CHOICES = (
        ('a', '4-4-2'),
        ('b', '3-5-2'),
        ('c', '3-4-3'),
        ('d', '4-5-1'),
    )
    TACTICS_CHOICES = (
        ('з', 'защитная'),
        ('н', 'нормальная'),
        ('а', 'атакующая'),
    )
    STYLE_CHOICES = (
        ('нрм', 'нормальный'),
        ('ббг', 'бей-беги'),
        ('брт', 'британский'),
        ('ктч', 'катеначчо'),
        ('спк', 'спартаковский'),
        ('брз', 'бразильский'),
        ('ттк', 'тики-така'),
    )
    PROTECTION_CHOICES = (
        ('и', 'по игроку'),
        ('з', 'зональный'),
    )
    MOOD_CHOICES = (
        ('о', 'отдых'),
        ('с', 'супер'),
    )
    POSITION_CHOICES = (
        ('GK', 'вратарь'),
        ('LD', 'левый защитник'),
        ('CD', 'центральный защитник'),
        ('RD', 'правый защитник'),
        ('LM', 'левый полузащитник'),
        ('CM', 'центральный полузащитник'),
        ('RM', 'правый полузащитник'),
        ('CF', 'центральный нападающий'),
    )
    formation_home = models.CharField(
        max_length=1,
        choices=FORMATION_CHOICES,
    )
    tactics_home = models.CharField(
        max_length=1,
        choices=TACTICS_CHOICES,
    )
    style_home = models.CharField(
        max_length=3,
        choices=STYLE_CHOICES,
    )
    protection_home = models.CharField(
        max_length=1,
        choices=PROTECTION_CHOICES,
    )
    mood_home = models.CharField(
        max_length=1,
        choices=MOOD_CHOICES,
    )
    score = models.CharField(
        max_length=255,
    )
    formation_guest = models.CharField(
        max_length=1,
        choices=FORMATION_CHOICES,
    )
    tactics_guest = models.CharField(
        max_length=1,
        choices=TACTICS_CHOICES,
    )
    style_guest = models.CharField(
        max_length=3,
        choices=STYLE_CHOICES,
    )
    protection_guest = models.CharField(
        max_length=1,
        choices=PROTECTION_CHOICES,
    )
    mood_guest = models.CharField(
        max_length=1,
        choices=MOOD_CHOICES,
    )
    position1_home = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position2_home = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position3_home = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position4_home = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position5_home = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position6_home = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position7_home = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position8_home = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position9_home = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position10_home = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position11_home = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position1_guest = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position2_guest = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position3_guest = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position4_guest = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position5_guest = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position6_guest = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position7_guest = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position8_guest = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position9_guest = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position10_guest = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    position11_guest = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    player1_home = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='home1',
    )
    player2_home = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='home2',
    )
    player3_home = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='home3',
    )
    player4_home = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='home4',
    )
    player5_home = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='home5',
    )
    player6_home = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='home6',
    )
    player7_home = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='home7',
    )
    player8_home = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='home8',
    )
    player9_home = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='home9',
    )
    player10_home = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='home10',
    )
    player11_home = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='home11',
    )
    player1_guest = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='guest1',
    )
    player2_guest = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='guest2',
    )
    player3_guest = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='guest3',
    )
    player4_guest = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='guest4',
    )
    player5_guest = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='guest5',
    )
    player6_guest = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='guest6',
    )
    player7_guest = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='guest7',
    )
    player8_guest = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='guest8',
    )
    player9_guest = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='guest9',
    )
    player10_guest = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='guest10',
    )
    player11_guest = models.OneToOneField(
        Player,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='guest11',
    )
