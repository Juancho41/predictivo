from pyexpat import model
from .models import Medicion
from django.forms import ModelForm

class MedicionForm(ModelForm):
    class Meta:
        model = Medicion
        fields = '__all__'
