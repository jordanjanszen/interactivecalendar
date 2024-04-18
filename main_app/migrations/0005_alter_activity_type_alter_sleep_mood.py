# Generated by Django 5.0.4 on 2024-04-18 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_activity_type_alter_sleep_mood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='type',
            field=models.CharField(choices=[('Run', 'Run'), ('Ride', 'Ride'), ('Swim', 'Swim'), ('Walk', 'Walk'), ('Gym', 'Gym'), ('Yoga', 'Yoga'), ('Other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='mood',
            field=models.CharField(choices=[('😊', 'Pleasant'), ('😐', 'Neutral'), ('😒', 'Unpleasant')], max_length=10),
        ),
    ]
