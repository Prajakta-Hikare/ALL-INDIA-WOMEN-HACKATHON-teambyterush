# forms.py
from django import forms
from .models import Patient

class PatientDataForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('hospital_name', 'address', 'speciality', 'contact_number', 'short_intro', 'email')
        

class CustomerDetailsForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    gender = forms.CharField(max_length=10)
    height = forms.FloatField()
    weight = forms.FloatField()
    healthIssues = forms.FloatField()
    email = forms.FloatField()
    tel = forms.IntegerField()
    
    

