# Generated by Django 3.0.8 on 2020-10-27 08:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20201027_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='categories',
            field=models.CharField(choices=[('MEN', 'Men'), ('FEMALE', 'Female'), ('KIDS', 'KIDS'), ('ACCESSORIES', 'Accessories'), ('CLOTHING', 'Clothing'), ('BAGS', 'Bags'), ('SHOES', 'Shoes')], default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 27, 11, 13, 22, 382242)),
        ),
    ]
