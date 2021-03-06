# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-18 13:30
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicfood', '0004_auto_20160918_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='healthy_level',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MaxValueValidator(99.99), django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='food',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='food',
            name='taste_level',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]
