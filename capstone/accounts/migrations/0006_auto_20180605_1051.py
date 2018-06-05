# Generated by Django 2.0.4 on 2018-06-05 15:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180605_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(blank=True, default=uuid.uuid4, max_length=10, unique=True),
        ),
    ]
