# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-30 21:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('launchscreen', '0013_auto_20190430_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='primaryinterest',
            old_name='checked',
            new_name='checker',
        ),
    ]