from django.contrib.auth.models import AbstractUser
from django.db import models

from main.dictionary import exp


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'M', exp('user.gender.male')
        FEMALE = 'F', exp('user.gender.female')
    gender = models.CharField(exp('user.gender'), choices=Gender.choices, max_length=1)
    bio = models.TextField(exp('user.bio'), blank=True)
    image = models.ImageField(exp('user.image'), null=True, default=None)
