# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-08 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchscreen', '0016_remove_major_credits_req'),
    ]

    operations = [
        migrations.AddField(
            model_name='major',
            name='credits_req',
            field=models.IntegerField(default=34),
        ),
    ]
