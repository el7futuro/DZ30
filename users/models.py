from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE = [
        ("member", "пользователь"),
        ("admin", "администратор"),
        ("moderator", "модератор")
    ]

    role = models.CharField(max_length=9, choices=ROLE, default="member")
    location = models.ManyToManyField('Location')
    age = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return self.username


class Location(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name


