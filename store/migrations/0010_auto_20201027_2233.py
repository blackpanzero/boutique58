# Generated by Django 3.0.8 on 2020-10-27 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20201027_1113'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hotel',
        ),
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 27, 22, 33, 13, 118503)),
        ),
    ]
