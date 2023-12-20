from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class Team(models.Model):
    '''Команда.'''
    name = models.CharField(
        verbose_name='Название команды',
        max_length=255,
    )
    city = models.CharField(
        verbose_name='Команда из города',
        max_length=255,
    )
    coach = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    emblem = models.ImageField(
        verbose_name='Эмблема клуба',
        upload_to='teams/',
        blank=True,
        null=True,
    )
    stadium = models.CharField(
        verbose_name='Название стадиона команды',
        max_length=255,
    )
    capacity = models.PositiveIntegerField(
        verbose_name='Вместимость стадиона',
        default=3500,
    )


class Player(models.Model):
    '''Футболист, футбольный игрок, персонаж.'''
    POSITION_CHOICES = (
        ('ВР', 'Вратарь'),
        ('ЗЩ', 'Защитник'),
        ('ПЗ', 'Полузащитник'),
        ('НП', 'Нападающий'),
    )
    COUNTRY_CHOICES = (
        ('RU', 'Россия'),
        ('EN', 'Англия'),
    )
    name = models.CharField(
        verbose_name='Футболист',
        max_length=255,
    )
    age = models.PositiveSmallIntegerField(
        verbose_name='Возраст футболиста',
        validators=(
            MaxValueValidator(settings.MAX_AGE_PLAYER, 'Сделай помоложе'),
            MinValueValidator(settings.MIN_AGE_PLAYER, 'Сделай постарше'),
        )
    )
    power = models.PositiveSmallIntegerField(
        verbose_name='Сила футболиста',
        validators=(
            MaxValueValidator(settings.MAX_POWER_PLAYER, 'Слишком сильный'),
            MinValueValidator(settings.MIN_POWER_PLAYER, 'Слишком слабый'),
        )
    )
    cost = models.PositiveIntegerField(
        verbose_name='Цена футболиста',
    )
    position = models.CharField(
        max_length=2,
        choices=POSITION_CHOICES,
    )
    country = models.CharField(
        max_length=2,
        choices=COUNTRY_CHOICES,
    )
    fatigue = models.PositiveSmallIntegerField(
        verbose_name='Усталость футболиста',
        default=0,
        editable=False,
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='players',
    )


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
