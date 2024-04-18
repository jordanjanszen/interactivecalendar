from django.forms import ModelForm
from .models import Nutrition

class NutritionForm(ModelForm):
    class Meta:
        model = Nutrition
        fields = '__all__'
        exclude = ['activity']

