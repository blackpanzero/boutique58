# Generated by Django 3.0.8 on 2020-11-11 11:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_auto_20201106_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 11, 14, 59, 24, 273830)),
        ),
    ]