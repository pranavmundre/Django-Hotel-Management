# Generated by Django 3.0 on 2020-04-01 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAdmin', '0023_auto_20200401_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='is_publish',
            field=models.BooleanField(default=False, null=True),
        ),
    ]