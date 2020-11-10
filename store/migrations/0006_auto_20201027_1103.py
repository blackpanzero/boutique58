# Generated by Django 3.0.8 on 2020-10-27 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20201027_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='categories',
            field=models.CharField(choices=[('men', 'men'), ('female', 'Female'), ('kids', 'KIDS'), ('accesories', 'Accesories'), ('clothing', 'Clothing'), ('bags', 'Bags'), ('shoes', 'Shoes')], default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 27, 11, 3, 56, 874771)),
        ),
    ]
