from .models import *
from django.forms import ModelForm

class llm_form(ModelForm):
    class Meta:
        model = llm_data
        fields = ('user','message','response')