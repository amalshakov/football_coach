from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''Расширенная модель пользователя.'''
    email = models.EmailField(
        verbose_name='email',
        max_length=settings.EMAIL_MAX_LENGTH,
        unique=True,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return f'{self.username}'
