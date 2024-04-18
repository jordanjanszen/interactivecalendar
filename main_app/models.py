from django.db import models
from django.urls import reverse

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    date = models.DateTimeField()
    type = models.CharField(max_length=25)
    time = models.DurationField()
    distance = models.IntegerField()
    elevationgain = models.IntegerField()
    calories = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('activities_detail', kwargs={'activity_id': self.id})

    class Meta:
        ordering = ['-date']


class Sleep(models.Model):
    date = models.DateField()
    bedtime = models.TimeField()
    awake = models.TimeField()
    mood = models.CharField(max_length=25)
    note = models.TextField(max_length=150)

    def get_absolute_url(self):
        return reverse('sleep_detail', kwargs={'sleep_id': self.id})

    class Meta:
        ordering = ['-date']
