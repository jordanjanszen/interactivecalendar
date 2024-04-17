from django.db import models

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateTimeField()
    
    ACTIVITY_TYPES = [
        ('Run', 'Run'),
        ('Ride', 'Ride'),
        ('Swim', 'Swim'),
        ('Walk', 'Walk'),
        ('Gym', 'Gym'),
        ('Yoga', 'Yoga'),
        ('Other', 'Other')
    ]
    type = models.CharField(max_length=50, choices=ACTIVITY_TYPES)
    time = models.DurationField()
    distance = models.IntegerField()
    elevationgain = models.IntegerField()
    calories = models.IntegerField()

    def __str__(self):
        return self.name

class Sleep(models.Model):
    date = models.DateField()
    bedtime = models.TimeField()
    awake = models.TimeField()
    WAKE_UP_MOOD = [
        ('😊', 'Pleasant'),
        ('😐', 'Neutral'),
        ('😒', 'Unpleasant'),
    ]
    mood = models.CharField(max_length=20, choices=WAKE_UP_MOOD)
    note = models.CharField(max_length=150)
