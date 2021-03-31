# Generated by Django 3.1.7 on 2021-03-31 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('attendance_app', '0001_initial'),
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancereport',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='course_app.course'),
        ),
    ]