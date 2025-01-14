# Generated by Django 5.1.3 on 2024-12-12 01:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LabEquipment',
            fields=[
                ('list_id', models.AutoField(primary_key=True, serialize=False, verbose_name='List ID')),
                ('instrument_id', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Instrument ID')),
                ('equipment_name', models.CharField(max_length=200, verbose_name='Equipment Name')),
                ('manufacturer_name', models.CharField(max_length=150, verbose_name='Manufacturer Name')),
                ('model_name', models.CharField(max_length=100, verbose_name='Model Name')),
                ('serial_number', models.CharField(max_length=100, unique=True, verbose_name='Serial Number')),
                ('date_of_manufacture', models.DateField(verbose_name='Date of Manufacture')),
                ('calibrated_by', models.CharField(max_length=150, verbose_name='Calibrated By')),
                ('calibration_certification_number', models.CharField(max_length=100, verbose_name='Calibration Certification Number')),
                ('calibration_date', models.DateField(verbose_name='Calibration Date')),
                ('calibration_due_date', models.DateField(verbose_name='Calibration Due Date')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='Remarks')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
            options={
                'verbose_name': 'Lab Equipment',
                'verbose_name_plural': 'Lab Equipments',
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['instrument_id'], name='LabEquipmen_instrum_7ca334_idx'), models.Index(fields=['serial_number'], name='LabEquipmen_serial__5e3415_idx'), models.Index(fields=['calibration_due_date'], name='LabEquipmen_calibra_ff1962_idx')],
            },
        ),
    ]
