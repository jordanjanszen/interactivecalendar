from django.shortcuts import render
from django.views.generic.edit import CreateView

# Import MODELS
from .models import Activity, Sleep

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def calendar_index(request):
  return render(request, 'calendar/index.html')



def activities_index(request):
  activities = Activity.objects.all()
  return render(request, 'activities/index.html', {
    'activities': activities
  })

def activities_detail(request, activity_id):
   activity = Activity.objects.get(id=activity_id)
   return render(request, 'activities/detail.html', {
      'activity': activity
   })

class ActivityCreate(CreateView):
   model = Activity
   fields = '__all__'


def sleep_index(request):
  sleeps = Sleep.objects.all()
  return render(request, 'sleep/index.html', {
    'sleeps': sleeps
  })

def sleep_detail(request, sleep_id):
   sleep = Sleep.objects.get(id=sleep_id)
   return render(request, 'sleep/detail.html', {
      'sleep': sleep
   })

class SleepCreate(CreateView):
   model = Sleep
   fields = '__all__'


def dashboard_index(request):
  return render(request, 'dashboard/index.html')