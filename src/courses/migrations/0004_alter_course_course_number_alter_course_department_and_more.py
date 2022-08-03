# Generated by Django 4.0.7 on 2022-08-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_first_day_alter_course_second_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_number',
            field=models.IntegerField(verbose_name='شماره درس'),
        ),
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.CharField(max_length=128, verbose_name='دانشکده'),
        ),
        migrations.AlterField(
            model_name='course',
            name='end_time',
            field=models.TimeField(verbose_name='ساعت پایان'),
        ),
        migrations.AlterField(
            model_name='course',
            name='first_day',
            field=models.IntegerField(choices=[(0, 'شنبه'), (1, 'یک\u200cشنبه'), (2, 'دوشنبه'), (3, 'سه\u200cشنبه'), (4, 'چهارشنبه')], default=0, verbose_name='روز اول'),
        ),
        migrations.AlterField(
            model_name='course',
            name='group_number',
            field=models.IntegerField(verbose_name='شماره گروه'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=128, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='course',
            name='second_day',
            field=models.IntegerField(blank=True, choices=[(None, 'ندارد'), (0, 'شنبه'), (1, 'یک\u200cشنبه'), (2, 'دوشنبه'), (3, 'سه\u200cشنبه'), (4, 'چهارشنبه')], default=None, null=True, verbose_name='روز دوم'),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_time',
            field=models.TimeField(verbose_name='ساعت شروع'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.CharField(max_length=128, verbose_name='نام استاد'),
        ),
    ]
