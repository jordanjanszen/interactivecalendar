from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('calendar/', views.calendar_index, name='calendar_index'),
    path('activities/', views.activities_index, name='activities_index'),
    path('activities/<int:activity_id>/', views.activities_detail, name='activities_detail'),
    path('sleep/', views.sleep_index, name='sleep_index'),
    path('sleep/<int:sleep_id>/', views.sleep_detail, name='sleep_detail'),
    path('dashboard', views.dashboard_index, name='dashboard_index'),
]