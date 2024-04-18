from django.contrib import admin

from .models import Activity, Sleep, Nutrition

# Register your models here.
admin.site.register(Activity)
admin.site.register(Sleep)
admin.site.register(Nutrition)