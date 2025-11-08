from  app1.models import Employees
from django import forms

class Employee_form(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'