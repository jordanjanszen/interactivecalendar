from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Import FORMS
from .forms import NutritionForm

# Import MODELS
from .models import Activity, Sleep

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('calendar_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def calendar_index(request):
  return render(request, 'calendar/index.html')


@login_required
def activities_index(request):
  activities = Activity.objects.filter(user=request.user)
  return render(request, 'activities/index.html', {
    'activities': activities
  })

@login_required
def activities_detail(request, activity_id):
   activity = Activity.objects.get(id=activity_id)
   nutrition_form = NutritionForm()
   return render(request, 'activities/detail.html', {
      'activity': activity,
      'nutrition_form': nutrition_form,
   })

class ActivityCreate(LoginRequiredMixin, CreateView):
    model = Activity
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class ActivityUpdate(LoginRequiredMixin, UpdateView):
  model = Activity
  fields = '__all__'

class ActivityDelete(LoginRequiredMixin, DeleteView):
  model = Activity
  success_url = '/activities'

@login_required
def add_nutrition(request, activity_id):
  form = NutritionForm(request.POST)
  if form.is_valid():
    new_nutrition = form.save(commit=False)
    new_nutrition.activity_id = activity_id
    new_nutrition.save()
  return redirect('activities_detail', activity_id=activity_id)

@login_required
def sleep_index(request):
  sleeps = Sleep.objects.filter(user=request.user)
  return render(request, 'sleep/index.html', {
    'sleeps': sleeps
  })

@login_required
def sleep_detail(request, sleep_id):
   sleep = Sleep.objects.get(id=sleep_id)
   return render(request, 'sleep/detail.html', {
      'sleep': sleep
   })

class SleepCreate(LoginRequiredMixin, CreateView):
    model = Sleep
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SleepUpdate(LoginRequiredMixin, UpdateView):
  model = Sleep
  fields = '__all__'

class SleepDelete(LoginRequiredMixin, DeleteView):
  model = Sleep
  success_url = '/sleep'

@login_required
def dashboard_index(request):
  return render(request, 'dashboard/index.html')
