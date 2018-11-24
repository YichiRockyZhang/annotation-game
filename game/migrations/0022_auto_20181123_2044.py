# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-11-24 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0021_auto_20181123_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='difficulty',
            field=models.TextField(default='HS'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='difficulty',
            field=models.CharField(choices=[('College', 'College'), ('MS', 'MS'), ('HS', 'HS')], default='HS', max_length=10),
        ),
        migrations.AlterField(
            model_name='player',
            name='last_seen',
            field=models.FloatField(default=1543023844.780381),
        ),
        migrations.AlterField(
            model_name='room',
            name='buzz_end_time',
            field=models.FloatField(default=1543023845.779378),
        ),
        migrations.AlterField(
            model_name='room',
            name='buzz_start_time',
            field=models.FloatField(default=1543023844.779378),
        ),
        migrations.AlterField(
            model_name='room',
            name='end_time',
            field=models.FloatField(default=1543023845.779378),
        ),
        migrations.AlterField(
            model_name='room',
            name='start_time',
            field=models.FloatField(default=1543023844.778378),
        ),
    ]
