# Generated by Django 5.0.4 on 2024-04-18 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_nutrition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='calories',
            field=models.IntegerField(verbose_name='Calories Burned'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateTimeField(verbose_name='Date (yyyy/mm/dd)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='distance',
            field=models.IntegerField(verbose_name='Distance (m)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='elevationgain',
            field=models.IntegerField(verbose_name='Elevation Gain (m)'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='time',
            field=models.DurationField(verbose_name='Activity Duration (hh:mm:ss)'),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='carbohydrates',
            field=models.IntegerField(verbose_name='Carbohydrates (g)'),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='fat',
            field=models.IntegerField(verbose_name='Fat (g)'),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='protein',
            field=models.IntegerField(verbose_name='Protein (g)'),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='totalcalories',
            field=models.IntegerField(verbose_name='Total Calories Consumed'),
        ),
        migrations.AlterField(
            model_name='sleep',
            name='date',
            field=models.DateField(verbose_name='Date (yyyy/mm/dd)'),
        ),
    ]