# Generated by Django 3.0 on 2021-03-31 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university_app', '0006_auto_20210331_1336'),
        ('users', '0002_remove_studentprofile_year_in_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='st_class',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='university_app.Class'),
        ),
    ]
