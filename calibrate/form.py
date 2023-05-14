from django import forms
from .models import *

class cal_form(forms.ModelForm):
    class Meta:
        model = clicks
        fields = ('user',"mouseX","mouseY","time_stamp","event")