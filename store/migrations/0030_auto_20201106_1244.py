# Generated by Django 3.0.8 on 2020-11-06 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_auto_20201106_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='categories',
            field=models.CharField(choices=[('DRESSES', 'Dresses'), ('TROUSERS', 'Trousers'), ('SWEATERS', 'Sweaters'), ('BLAZERS', 'Blazers'), ('ROMPERS', 'Rompers'), ('T-SHIRTS', 'T-shirts'), ('TOPS', 'Tops'), ('BOOTS', 'Boots'), ('HEALS', 'Heals'), ('SNEAKERS', 'Sneaks'), ('SUNGLASSES', 'Sunglasses'), ('UNDERWARE', 'Underware'), ('BAGS', 'Bags'), ('HEELS', 'Heels'), ('SNEAKERS', 'Sneakers')], default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='item',
            name='category_type',
            field=models.CharField(choices=[('ACCESSORIES', 'Accessories'), ('CLOTHING', 'Clothing'), ('SHOES', 'Shoes')], default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 6, 12, 44, 55, 435696)),
        ),
    ]
