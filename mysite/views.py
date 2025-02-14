from django.http import HttpResponse
from django.shortcuts import render , redirect
from employees.models import Employee
from .forms import RegistrationForm 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from .employee_forms import EmployeeForm

def home(request):
    query = request.GET.get('q')
    if query:
        employees = Employee.objects.filter(first_name__icontains=query) | Employee.objects.filter(last_name__icontains=query)
    else:
        employees = Employee.objects.all()
        
    context = {
        'employees' : employees,
        'query': query,
    }
    return render(request, 'home.html', context)


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user     = auth.authenticate(username=username, password=password)   
            
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    
    context = {
        'form': form,
    }
    return render(request, 'add_employee.html', context)

