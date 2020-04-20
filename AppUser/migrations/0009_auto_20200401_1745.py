# Generated by Django 3.0 on 2020-04-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUser', '0008_auto_20200401_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='gender',
            field=models.CharField(blank=True, choices=[(1, 'Male'), (0, 'Female'), (2, 'Other')], max_length=1, null=True),
        ),
    ]
