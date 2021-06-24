from django import forms
from .models import Company, Employee

class CompanyForm(forms.ModelForm):
    
    class Meta:
        model = Company
        fields = ("name",)
        
class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ("name",)
