# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-29 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchscreen', '0011_major_tag_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='primaryinterest',
            name='selected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='secondaryinterest',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]
