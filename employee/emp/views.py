from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee
from .forms import EmployeeForm

# List all employees
class EmployeeListView(ListView):
    model = Employee
    template_name = 'emp/employee_list.html'
    context_object_name = 'employees'

# View employee details
class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'emp/employee_detail.html'
    context_object_name = 'employee'
    pk_url_kwarg = 'employee_id'

# Create a new employee
class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'emp/employee_form.html'
    success_url = reverse_lazy('employee-list')

# Update an employee
class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'emp/employee_form.html'
    success_url = reverse_lazy('employee-list')
    pk_url_kwarg = 'employee_id'

# Delete an employee
class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'emp/employee_confirm_delete.html'
    success_url = reverse_lazy('employee-list')
    pk_url_kwarg = 'employee_id'