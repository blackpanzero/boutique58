# Generated by Django 3.0.8 on 2020-11-04 12:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_auto_20201104_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 4, 15, 10, 59, 945450)),
        ),
    ]
