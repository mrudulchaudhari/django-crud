from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'phone_number', 'birth_date', 'role']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }