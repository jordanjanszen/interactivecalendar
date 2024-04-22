from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('calendar/', views.calendar_index, name='calendar_index'),
    path('activities/', views.activities_index, name='activities_index'),
    path('activities/<int:activity_id>/', views.activities_detail, name='activities_detail'),
    path('activities/create/', views.ActivityCreate.as_view(), name='activities_create'),
    path('activities/<int:pk>/update/', views.ActivityUpdate.as_view(), name='activities_update'),
    path('activities/<int:pk>/delete/', views.ActivityDelete.as_view(), name='activities_delete'),
    path('activities/<int:activity_id>/add_nutrition/', views.add_nutrition, name='add_nutrition'),
    path('sleep/', views.sleep_index, name='sleep_index'),
    path('sleep/<int:sleep_id>/', views.sleep_detail, name='sleep_detail'),
    path('sleep/create/', views.SleepCreate.as_view(), name='sleep_create'),
    path('sleep/<int:pk>/update/', views.SleepUpdate.as_view(), name='sleep_update'),
    path('sleep/<int:pk>/delete/', views.SleepDelete.as_view(), name='sleep_delete'),
    path('dashboard', views.dashboard_index, name='dashboard_index'),
    path('accounts/signup/', views.signup, name='signup'),
]