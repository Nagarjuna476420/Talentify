# Generated by Django 5.0.6 on 2024-07-29 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0003_alter_jobseeker_job_seeker_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='job_seeker_id',
            field=models.CharField(default='jB9QXjVXpW', max_length=10, unique=True),
        ),
    ]