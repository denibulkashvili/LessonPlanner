# Generated by Django 2.2 on 2019-04-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_plans', '0010_lesson_lesson_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='lesson_objectives',
            field=models.TextField(default='', max_length=500, verbose_name='lesson objectives'),
        ),
    ]
