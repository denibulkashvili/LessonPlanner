# Generated by Django 2.2 on 2019-04-14 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("lesson_plans", "0004_auto_20190414_1635")]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="lesson_number",
            field=models.IntegerField(max_length=10, verbose_name="lesson number"),
        )
    ]
