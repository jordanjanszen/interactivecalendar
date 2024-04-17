# Generated by Django 5.0.4 on 2024-04-16 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('bedtime', models.TimeField()),
                ('awake', models.TimeField()),
                ('mood', models.CharField(choices=[('😊', 'Pleasant'), ('😐', 'Neutral'), ('😒', 'Unpleasant')], max_length=20)),
                ('note', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='activity',
            name='time',
            field=models.DurationField(),
        ),
    ]
