from django.db import models

# Create your models here.
# employee_register/models.py
class Employee(models.Model):
    ROLE_CHOICES = [
        ('IT', 'IT'),
        ('Developer', 'Developer'),
        ('Admin', 'Admin'),
        ('Accounts', 'Accounts'),
    ]
    
    empid = models.CharField(max_length=10, primary_key=True)  # This should be emp_code, not empid
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.empid})"