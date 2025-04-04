from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'phone_number', 'birth_date', 'role')
    search_fields = ('name', 'employee_id', 'role')
    list_filter = ('role',)