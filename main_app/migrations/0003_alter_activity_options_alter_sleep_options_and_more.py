# Generated by Django 5.0.4 on 2024-04-17 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_sleep_alter_activity_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='sleep',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='activity',
            name='type',
            field=models.CharField(choices=[('Run', 'Run'), ('Ride', 'Ride'), ('Swim', 'Swim'), ('Walk', 'Walk'), ('Gym', 'Gym'), ('Yoga', 'Yoga'), ('Other', 'Other')], max_length=5),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='mood',
            field=models.CharField(choices=[('😊', 'Pleasant'), ('😐', 'Neutral'), ('😒', 'Unpleasant')], max_length=1),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='note',
            field=models.TextField(max_length=150),
        ),
    ]
