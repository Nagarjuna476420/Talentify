# Generated by Django 5.0.6 on 2024-07-19 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='job_seeker_id',
            field=models.CharField(default='jyYyAOZCB2', max_length=10, unique=True),
        ),
    ]