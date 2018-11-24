# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-11-24 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0022_auto_20181123_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='last_seen',
            field=models.FloatField(default=1543029219.26391),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.TextField(default='Everything'),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.TextField(default='HS'),
        ),
        migrations.AlterField(
            model_name='room',
            name='buzz_end_time',
            field=models.FloatField(default=1543029220.262913),
        ),
        migrations.AlterField(
            model_name='room',
            name='buzz_start_time',
            field=models.FloatField(default=1543029219.262913),
        ),
        migrations.AlterField(
            model_name='room',
            name='end_time',
            field=models.FloatField(default=1543029220.262913),
        ),
        migrations.AlterField(
            model_name='room',
            name='start_time',
            field=models.FloatField(default=1543029219.262913),
        ),
    ]
