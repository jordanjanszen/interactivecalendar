from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    date = models.DateField('Date (yyyy-mm-dd)')
    type = models.CharField(max_length=25)
    time = models.DurationField('Activity Duration (hh:mm:ss)')
    distance = models.IntegerField('Distance (m)')
    elevationgain = models.IntegerField('Elevation Gain (m)')
    calories = models.IntegerField('Calories Burned')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('activities_detail', kwargs={'activity_id': self.id})

    class Meta:
        ordering = ['-date']

    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Nutrition(models.Model):
    name = models.CharField(max_length=75, default='N/A')
    fat = models.IntegerField('Fat (g)')
    protein = models.IntegerField('Protein (g)')
    carbohydrates = models.IntegerField('Carbohydrates (g)')
    totalcalories = models.IntegerField('Total Calories Consumed')

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

class Sleep(models.Model):
    date = models.DateField('Date (yyyy-mm-dd)')
    bedtime = models.TimeField()
    awake = models.TimeField()
    mood = models.CharField(max_length=25)
    note = models.TextField(max_length=150)

    def get_absolute_url(self):
        return reverse('sleep_detail', kwargs={'sleep_id': self.id})

    class Meta:
        ordering = ['-date']

    user = models.ForeignKey(User, on_delete=models.CASCADE)
