# Generated by Django 2.2 on 2019-04-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_plans', '0009_auto_20190414_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lesson_duration',
            field=models.IntegerField(default=0, verbose_name='lesson duration (in minutes)'),
        ),
    ]
