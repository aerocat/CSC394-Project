# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-12 00:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_search', '0014_auto_20180412_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursewithnorequirements',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course_search.AdvancedCourse'),
        ),
    ]
