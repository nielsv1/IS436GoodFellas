# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-25 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchscreen', '0003_auto_20190425_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uni_class',
            name='class_name',
            field=models.CharField(max_length=600),
        ),
    ]
