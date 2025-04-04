from django.db import models

class Employee(models.Model):
    ROLE_CHOICES = [
        ('accounts', 'Accounts'),
        ('it', 'IT'),
        ('dev', 'Development'),
        ('admin', 'Admin'),
    ]
    
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    def __str__(self):
        return f"{self.name} ({self.employee_id})"