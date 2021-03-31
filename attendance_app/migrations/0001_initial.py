# Generated by Django 3.0 on 2021-03-31 05:55

import attendance_app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=attendance_app.models.current_time)),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='attendance_app.Attendance')),
            ],
        ),
    ]
