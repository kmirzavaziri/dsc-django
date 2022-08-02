from django.db import models


class Course(models.Model):
    class WeekDay(models.TextChoices):
        SATURDAY = '0'
        SUNDAY = '1'
        MONDAY = '2'
        TUESDAY = '3'
        WEDNESDAY = '4'

    department = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=128)
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = models.IntegerField(choices=WeekDay.choices)
    second_day = models.IntegerField(choices=WeekDay.choices)

    def __str__(self):
        return self.name
