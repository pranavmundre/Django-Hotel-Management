# Generated by Django 3.0 on 2020-04-04 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAdmin', '0029_auto_20200405_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomorder',
            name='order_no',
            field=models.CharField(blank=True,   max_length=255, null=True, unique=True),
        ),
    ]
