from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):  # Renamed from User to Employees
    EMPLOYEE_TYPES = [
        ('sales', 'Sales'),
        ('supervisor', 'Supervisor'),
        ('technician', 'Technician'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    ]

    CONTRACT_TYPES = [
        ('permanent', 'Permanent'),
        ('temporary', 'Temporary'),
        ('contract', 'Contract'),
    ]

    OVERTIME_TYPES = [
        ('fixed', 'Fixed'),
        ('variable', 'Variable'),
        ('automatic', 'Automatic'),
    ]

    # Basic Information
    emp_type = models.CharField(max_length=20, choices=EMPLOYEE_TYPES, blank=True, null=True, default=None)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    employee_id = models.CharField(max_length=20, unique=True, blank=True, null=True, default=None)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True, default=None)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, blank=True, null=True, default=None)
    nationality = models.CharField(max_length=50, blank=True, null=True, default=None)
    
    # Employment Details
    branch_name = models.CharField(max_length=100, blank=True, null=True, default=None)
    department = models.CharField(max_length=100, blank=True, null=True, default=None)
    position = models.CharField(max_length=100, blank=True, null=True, default=None)
    contract_type = models.CharField(max_length=20, choices=CONTRACT_TYPES, blank=True, null=True, default=None)
    joining_date = models.DateField(blank=True, null=True, default=None)
    employment_status = models.CharField(max_length=50, blank=True, null=True, default=None)
    line_manager = models.CharField(max_length=100, blank=True, null=True, default=None)
    contract_duration = models.IntegerField(help_text="Duration in months", blank=True, null=True, default=None)
    contract_issuance_date = models.DateField(blank=True, null=True, default=None)
    contract_expiry_date = models.DateField(blank=True, null=True, default=None)
    contracted_hours_per_day = models.FloatField(blank=True, null=True, default=None)

    # Salary & Allowances
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=None)
    house_allowance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=None)
    transport_allowance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=None)
    food_allowance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=None)
    other_allowance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=None)
    gosi_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=None)
    total_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=None)

    # Overtime
    overtime_type = models.CharField(max_length=20, choices=OVERTIME_TYPES, blank=True, null=True, default=None)
    overtime_hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=None)

    # Leave
    leave_entitlement = models.IntegerField(help_text="Number of leave days per year", blank=True, null=True, default=None)

    # GOSI Information
    gosi_number = models.CharField(max_length=20, unique=True, blank=True, null=True, default=None)
    saudi_arrival_date = models.DateField(blank=True, null=True, default=None)

    # Identification Details
    id_type = models.CharField(max_length=50, blank=True, null=True, default=None)
    id_number = models.CharField(max_length=50, unique=True, blank=True, null=True, default=None)
    name_in_id_english = models.CharField(max_length=100, blank=True, null=True, default=None)
    name_in_id_arabic = models.CharField(max_length=100, blank=True, null=True, default=None)
    id_issue_date = models.DateField(blank=True, null=True, default=None)
    id_expiry_date = models.DateField(blank=True, null=True, default=None)
    id_issue_place = models.CharField(max_length=100, blank=True, null=True, default=None)
    iqama_profession = models.CharField(max_length=100, blank=True, null=True, default=None)
    id_file = models.FileField(upload_to='id_documents/', blank=True, null=True)

    # Passport Details
    passport_number = models.CharField(max_length=50, unique=True, blank=True, null=True, default=None)
    passport_name = models.CharField(max_length=100, blank=True, null=True, default=None)
    passport_issue_date = models.DateField(blank=True, null=True, default=None)
    passport_expiry_date = models.DateField(blank=True, null=True, default=None)
    passport_issue_place = models.CharField(max_length=100, blank=True, null=True, default=None)
    passport_file = models.FileField(upload_to='passport_documents/', blank=True, null=True)

    # Driving License
    local_driving_license_number = models.CharField(max_length=50, blank=True, null=True, default=None)
    local_driving_license_expiry = models.DateField(blank=True, null=True, default=None)
    local_driving_license_file = models.FileField(upload_to='license_documents/', blank=True, null=True)

    # Banking Details
    bank_name = models.CharField(max_length=100, blank=True, null=True, default=None)
    account_number = models.CharField(max_length=50, unique=True, blank=True, null=True, default=None)
    iban = models.CharField(max_length=50, unique=True, blank=True, null=True, default=None)

    class Meta:
        db_table = "employees"  # Explicitly set the table name

    def __str__(self):
        return f"{self.username} - {self.employee_id if self.employee_id else 'N/A'}"
