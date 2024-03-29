# Generated by Django 3.0.8 on 2020-11-04 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_auto_20201104_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='categories',
            field=models.CharField(choices=[('ACCESSORIES', 'Accessories'), ('CLOTHING', 'Clothing'), ('BAGS', 'Bags'), ('SHOES', 'Shoes'), ('DRESSES', 'Dresses'), ('TROUSERS', 'Trousers'), ('SWEATERS', 'Sweaters'), ('COATS & BLAZERS', 'Coats & Blazers'), ('ROMPERS', 'Rompers'), ('T-SHIRTS', 'T-shirts'), ('TOPS', 'Tops')], default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 4, 14, 46, 54, 180120)),
        ),
    ]
