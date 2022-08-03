# Generated by Django 4.1 on 2022-08-03 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_type_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('T', 'استاد'), ('S', 'دانشجو')], default='S', max_length=1, verbose_name='نوع حساب'),
        ),
    ]