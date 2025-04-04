from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee
from .forms import EmployeeForm

# List all employees
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_register/employee_list.html'
    context_object_name = 'employees'

# View a single employee
class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_register/employee_detail.html'
    context_object_name = 'employee'

# Create a new employee
class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_register/employee_form.html'
    success_url = reverse_lazy('employee-list')
    
    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)
        
    def form_valid(self, form):
        print("Form is valid")
        return super().form_valid(form)

# Update an employee
class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_register/employee_form.html'
    success_url = reverse_lazy('employee-list')

# Delete an employee
class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_register/employee_confirm_delete.html'
    success_url = reverse_lazy('employee-list')