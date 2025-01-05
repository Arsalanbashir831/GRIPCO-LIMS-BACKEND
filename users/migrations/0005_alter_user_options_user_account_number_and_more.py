# Generated by Django 5.1.3 on 2025-01-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_plaintext_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AddField(
            model_name='user',
            name='account_number',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='bank_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='basic_salary',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='branch_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='contract_duration',
            field=models.IntegerField(blank=True, default=None, help_text='Duration in months', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='contract_expiry_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='contract_issuance_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='contract_type',
            field=models.CharField(blank=True, choices=[('permanent', 'Permanent'), ('temporary', 'Temporary'), ('contract', 'Contract')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='contracted_hours_per_day',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='employee_id',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='employment_status',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='food_allowance',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gosi_number',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gosi_salary',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='house_allowance',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='iban',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='id_expiry_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='id_file',
            field=models.FileField(blank=True, null=True, upload_to='id_documents/'),
        ),
        migrations.AddField(
            model_name='user',
            name='id_issue_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='id_issue_place',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='id_number',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='id_type',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='iqama_profession',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='joining_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='leave_entitlement',
            field=models.IntegerField(blank=True, default=None, help_text='Number of leave days per year', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='line_manager',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='local_driving_license_expiry',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='local_driving_license_file',
            field=models.FileField(blank=True, null=True, upload_to='license_documents/'),
        ),
        migrations.AddField(
            model_name='user',
            name='local_driving_license_number',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='name_in_id_arabic',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='name_in_id_english',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='nationality',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='other_allowance',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='overtime_hourly_rate',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='overtime_type',
            field=models.CharField(blank=True, choices=[('fixed', 'Fixed'), ('variable', 'Variable'), ('automatic', 'Automatic')], default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='passport_expiry_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='passport_file',
            field=models.FileField(blank=True, null=True, upload_to='passport_documents/'),
        ),
        migrations.AddField(
            model_name='user',
            name='passport_issue_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='passport_issue_place',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='passport_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='passport_number',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='saudi_arrival_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='total_salary',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='transport_allowance',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='emp_type',
            field=models.CharField(blank=True, choices=[('sales', 'Sales'), ('supervisor', 'Supervisor'), ('technician', 'Technician')], default=None, max_length=20, null=True),
        ),
        migrations.AlterModelTable(
            name='user',
            table='employees',
        ),
    ]