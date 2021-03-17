# Generated by Django 3.1.7 on 2021-03-17 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrolled',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolls', to='users.student'),
        ),
        migrations.AddField(
            model_name='courseapprove',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_approve', to='users.student'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='courses', to='users.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_list', to='users.teacher'),
        ),
        migrations.AlterUniqueTogether(
            name='enrolled',
            unique_together={('course_id', 'student_id')},
        ),
    ]
