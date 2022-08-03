from django.db import models

from main.dictionary import exp


class Course(models.Model):
    class WeekDay(models.IntegerChoices):
        SATURDAY = 0, exp('week_day.saturday')
        SUNDAY = 1, exp('week_day.sunday')
        MONDAY = 2, exp('week_day.monday')
        TUESDAY = 3, exp('week_day.tuesday')
        WEDNESDAY = 4, exp('week_day.wednesday')

    department = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=128)
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = models.IntegerField(choices=WeekDay.choices, null=False, default=WeekDay.SATURDAY)
    second_day = models.IntegerField(
        choices=[(None, exp('week_day.blank'))] + WeekDay.choices,
        null=True, blank=True, default=None
    )

    def __str__(self):
        return self.name
