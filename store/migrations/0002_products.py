# Generated by Django 3.0.8 on 2020-10-26 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Product_Img', models.ImageField(upload_to='images/')),
                ('Price', models.IntegerField()),
                ('categories', models.CharField(default='', max_length=64)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 10, 26, 10, 30, 1, 594076))),
            ],
        ),
    ]
