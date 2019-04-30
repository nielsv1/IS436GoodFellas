# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-29 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchscreen', '0009_auto_20190429_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='related_primary_interest',
        ),
        migrations.AddField(
            model_name='course',
            name='related_primary_interest',
            field=models.ManyToManyField(to='launchscreen.PrimaryInterest'),
        ),
        migrations.RemoveField(
            model_name='course',
            name='related_secondary_interest',
        ),
        migrations.AddField(
            model_name='course',
            name='related_secondary_interest',
            field=models.ManyToManyField(to='launchscreen.SecondaryInterest'),
        ),
        migrations.RemoveField(
            model_name='major',
            name='related_primary_interest',
        ),
        migrations.AddField(
            model_name='major',
            name='related_primary_interest',
            field=models.ManyToManyField(to='launchscreen.PrimaryInterest'),
        ),
        migrations.RemoveField(
            model_name='major',
            name='related_secondary_interest',
        ),
        migrations.AddField(
            model_name='major',
            name='related_secondary_interest',
            field=models.ManyToManyField(to='launchscreen.SecondaryInterest'),
        ),
    ]
