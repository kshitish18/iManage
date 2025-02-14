from django import forms
from employees.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'designation', 'email_address', 'phone_number', 'photo']