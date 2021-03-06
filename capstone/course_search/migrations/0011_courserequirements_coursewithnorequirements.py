# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-12 00:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_search', '0010_course_one_prerequisite'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseRequirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course_search.Course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseWithNoRequirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_code', models.CharField(max_length=10, null=True)),
                ('class_title', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
