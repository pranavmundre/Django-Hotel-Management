# Generated by Django 3.0 on 2020-03-19 19:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppAdmin', '0015_auto_20200320_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomorder',
            name='order_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]