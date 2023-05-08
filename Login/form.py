from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class registration_form(UserCreationForm):
    def __init(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)
        self.fields['username'].widget.attrs.update({
            'name':'username',
            'id':'username',
            'type':'text',
            'class':'form-input',
            'placeholder':'username',
            'maxlength':'16',
            'minlength':'6'
        })
        self.fields['email'].widget.attrs.update({
            'name':'email',
            'id':'email',
            'type':'email',
            'class':'form-input',
            'placeholder':'johndoe@mail.com',
            'maxlength':'16',
            'minlength':'6'
        })
        self.fields['first_name'].widget.attrs.update({
            'name':'first_name',
            'id':'first_name',
            'type':'text',
            'class':'form-input',
            'placeholder':'John',
            'maxlength':'16',
            'minlength':'6'
        })
        self.fields['last_name'].widget.attrs.update({
            'name':'last_name',
            'id':'last_name',
            'type':'text',
            'class':'form-input',
            'placeholder':'Doe',
            'maxlength':'16',
            'minlength':'6'
        })
        self.fields['password1'].widget.attrs.update({
            'name':'password1',
            'id':'password1',
            'type':'password1',
            'class':'form-input',
            'placeholder':'password',
            'maxlength':'16',
            'minlength':'6'
        })
        self.fields['password2'].widget.attrs.update({
            'name':'password2',
            'id':'password2',
            'type':'password',
            'class':'form-input',
            'placeholder':'confirm',
            'maxlength':'16',
            'minlength':'6'
        })


    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')