# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-07-24 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='locked_out',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
