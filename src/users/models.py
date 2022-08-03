from django.contrib.auth.models import AbstractUser
from django.db import models

from main.dictionary import exp


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'M', exp('user.gender.male')
        FEMALE = 'F', exp('user.gender.female')

    class Type(models.TextChoices):
        TEACHER = 'T', exp('user.type.teacher')
        STUDENT = 'S', exp('user.type.student')

    gender = models.CharField(exp('user.gender'), choices=Gender.choices, max_length=1)
    bio = models.TextField(exp('user.bio'), blank=True)
    image = models.ImageField(exp('user.image'), null=True, default=None)
    type = models.CharField(exp('user.type'), choices=Type.choices, max_length=1, default=Type.STUDENT)
