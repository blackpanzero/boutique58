# Generated by Django 3.0.8 on 2020-10-28 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20201027_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='gender',
            field=models.CharField(choices=[('MEN', 'Men'), ('FEMALE', 'Female'), ('KIDS', 'KIDS')], default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='item',
            name='categories',
            field=models.CharField(choices=[('ACCESSORIES', 'Accessories'), ('CLOTHING', 'Clothing'), ('BAGS', 'Bags'), ('SHOES', 'Shoes')], default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 28, 15, 8, 27, 630622)),
        ),
    ]
