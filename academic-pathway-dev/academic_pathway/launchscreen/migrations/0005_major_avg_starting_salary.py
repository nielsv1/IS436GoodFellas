# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-25 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchscreen', '0004_auto_20190425_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='major',
            name='avg_starting_salary',
            field=models.CharField(choices=[('30,000 - 50,000', 'low'), ('50,000 - 80,000', 'med'), ('80,000+', 'high')], default='med', max_length=20),
        ),
    ]