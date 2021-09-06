from . models import PatientDetail
from django.forms import ModelForm
from django import forms
class appoimentform(ModelForm):
    class Meta:
        model=PatientDetail
        fields=('name','email','phone','department','date','message')

        widgets = {
            'name':forms.TextInput(attrs={ 'class':'form-control '}),
            'email':forms.TextInput(attrs={ 'class':'form-control '}),
            'phone':forms.TextInput(attrs={ 'class':'form-control '}),
            'department':forms.Select(attrs={ 'class':'form-control '}),
            'date':forms.DateTimeInput(attrs={ 'class':'form-control'}),
            'message':forms.Textarea(attrs={ 'class':'form-control'}),
        }