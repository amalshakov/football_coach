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
        related_name='team',
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
        default=5000,
    )
    money = models.PositiveIntegerField(
        verbose_name='Деньги на счету команды',
        default=25000000,
    )

    def __str__(self) -> str:
        return self.name


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

    def calculate_cost(self):
        """Считает цену игрока."""
        return (40 - self.age) * self.power * 1000
