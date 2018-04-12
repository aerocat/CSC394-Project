# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-12 00:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_search', '0013_auto_20180412_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvancedCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_code', models.CharField(max_length=10, null=True)),
                ('class_title', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='one_prerequisite',
        ),
        migrations.RemoveField(
            model_name='courserequirements',
            name='parent',
        ),
        migrations.AlterModelOptions(
            name='coursewithnorequirements',
            options={'verbose_name': 'Course With No Requirements', 'verbose_name_plural': 'Courses With No Requirements'},
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='CourseRequirements',
        ),
        migrations.AddField(
            model_name='coursewithnorequirements',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course_search.AdvancedCourse'),
        ),
    ]
