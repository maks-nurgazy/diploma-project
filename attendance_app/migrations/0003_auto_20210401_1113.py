# Generated by Django 3.0.12 on 2021-04-01 05:13

import attendance_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_app', '0002_auto_20210331_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=attendance_app.models.current_time),
        ),
    ]
