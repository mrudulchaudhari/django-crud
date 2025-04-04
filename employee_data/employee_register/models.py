from django.db import models

# Create your models here.
class Employee(models.Model):
    ROLE_CHOICE = [
        ('IT', 'IT'),
        ('Developer', 'Developer'),
        ('Admin', 'Admin'),
        ('Accounts', 'Accounts'),
    ]
    empid = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length = 60)
    number = models.CharField(max_length=10, blank= False)
    role = models.CharField(max_length=20, choices = ROLE_CHOICE)

    def __str__(self):
        return f"{self.name} ({self.empid})"