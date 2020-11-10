# Generated by Django 3.0.8 on 2020-10-27 08:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20201027_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='categories',
            field=models.CharField(choices=[('MEN', 'Men'), ('FEM', 'Female'), ('KID', 'KIDS'), ('ACC', 'Accesories'), ('CLO', 'Clothing'), ('BAG', 'Bags'), ('SHO', 'Shoes')], default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 27, 11, 10, 16, 359433)),
        ),
    ]
