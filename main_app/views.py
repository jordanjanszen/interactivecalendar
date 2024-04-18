from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Import FORMS
from .forms import NutritionForm

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
   nutrition_form = NutritionForm()
   return render(request, 'activities/detail.html', {
      'activity': activity,
      'nutrition_form': nutrition_form,
   })

class ActivityCreate(CreateView):
   model = Activity
   fields = '__all__'

class ActivityUpdate(UpdateView):
  model = Activity
  fields = '__all__'

class ActivityDelete(DeleteView):
  model = Activity
  success_url = '/activities'

def add_nutrition(request, activity_id):
  form = NutritionForm(request.POST)
  if form.is_valid():
    new_nutrition = form.save(commit=False)
    new_nutrition.activity_id = activity_id
    new_nutrition.save()
  return redirect('activities_detail', activity_id=activity_id)


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

class SleepUpdate(UpdateView):
  model = Sleep
  fields = '__all__'

class SleepDelete(DeleteView):
  model = Sleep
  success_url = '/sleep'

def dashboard_index(request):
  return render(request, 'dashboard/index.html')