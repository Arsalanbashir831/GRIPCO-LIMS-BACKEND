# Generated by Django 5.1.3 on 2024-12-20 11:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LabEquipments', '0002_remove_labequipment_labequipmen_calibra_ff1962_idx_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalibrationList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calibrated_by', models.CharField(max_length=150, verbose_name='Calibrated By')),
                ('calibration_certification_number', models.CharField(max_length=100, verbose_name='Calibration Certification Number')),
                ('calibration_date', models.DateField(verbose_name='Calibration Date')),
                ('calibration_due_date', models.DateField(verbose_name='Calibration Due Date')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='Remarks')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calibrations', to='LabEquipments.labequipment', verbose_name='instrument_id')),
            ],
            options={
                'verbose_name': 'Calibration Record',
                'verbose_name_plural': 'Calibration Records',
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['instrument'], name='calibration_instrum_d4b740_idx'), models.Index(fields=['calibration_due_date'], name='calibration_calibra_e505e3_idx')],
            },
        ),
    ]
