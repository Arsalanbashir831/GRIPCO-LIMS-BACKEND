from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    EMPLOYEE_TYPES = [
        ('sales', 'Sales'),
        ('supervisor', 'Supervisor'),
        ('technician', 'Technician'),
    ]
    
    emp_type = models.CharField(max_length=20, choices=EMPLOYEE_TYPES, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.username
