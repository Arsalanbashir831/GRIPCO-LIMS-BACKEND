# Generated by Django 5.1.3 on 2024-12-19 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LabEquipments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='labequipment',
            name='LabEquipmen_calibra_ff1962_idx',
        ),
        migrations.RemoveField(
            model_name='labequipment',
            name='calibrated_by',
        ),
        migrations.RemoveField(
            model_name='labequipment',
            name='calibration_certification_number',
        ),
        migrations.RemoveField(
            model_name='labequipment',
            name='calibration_date',
        ),
        migrations.RemoveField(
            model_name='labequipment',
            name='calibration_due_date',
        ),
        migrations.RemoveField(
            model_name='labequipment',
            name='remarks',
        ),
    ]
