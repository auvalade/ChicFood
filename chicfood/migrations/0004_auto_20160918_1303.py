# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-18 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicfood', '0003_auto_20160918_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='healthy_level',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='food',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='short_desc',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='food',
            name='taste_level',
            field=models.IntegerField(),
        ),
    ]
