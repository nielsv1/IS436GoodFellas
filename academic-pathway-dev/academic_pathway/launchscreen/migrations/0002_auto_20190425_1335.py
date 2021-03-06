# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-25 17:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('launchscreen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='primaryInterests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_load', models.IntegerField()),
                ('avg_starting_salary', models.CharField(choices=[('30,000 - 50,000', 'low'), ('50,000 - 80,000', 'med'), ('80,000+', 'high')], default='med', max_length=20)),
                ('interest_1', models.CharField(choices=[('Technology', 'tech'), ('Healthcare', 'health'), ('Artistic Expression', 'art'), ('Mathematics', 'math'), ('Science', 'science')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='secondaryInterests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_2', models.CharField(choices=[('Exercise', 'exercise'), ('Travel', 'travel'), ('Hands-on', 'manual'), ('Critical Thinking', 'crit_think')], max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='major',
            name='avg_starting_salary',
        ),
        migrations.AlterField(
            model_name='major',
            name='major_major_interest_tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='major_major_interest_tag', to='launchscreen.primaryInterests'),
        ),
        migrations.AlterField(
            model_name='major',
            name='major_minor_interest_tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='major_minor_interest_tag', to='launchscreen.secondaryInterests'),
        ),
        migrations.AlterField(
            model_name='uni_class',
            name='class_major_interest_tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_major_interest_tag', to='launchscreen.primaryInterests'),
        ),
        migrations.AlterField(
            model_name='uni_class',
            name='class_minor_interest_tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_minor_interest_tag', to='launchscreen.secondaryInterests'),
        ),
        migrations.DeleteModel(
            name='Interests',
        ),
    ]
