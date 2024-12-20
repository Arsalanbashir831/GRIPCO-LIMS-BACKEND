from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

class LabEquipment(models.Model):

    list_id = models.AutoField(
        primary_key=True,
        verbose_name=_('List ID')
    )
    instrument_id = models.CharField(
        max_length=50,
        unique=True,
        validators=[MinLengthValidator(3)],
        verbose_name=_('Instrument ID')
    )
    
    equipment_name = models.CharField(
        max_length=200,
        verbose_name=_('Equipment Name')
    )
    
    manufacturer_name = models.CharField(
        max_length=150,
        verbose_name=_('Manufacturer Name')
    )
    model_name = models.CharField(
        max_length=100,
        verbose_name=_('Model Name')
    )
    
    serial_number = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('Serial Number')
    )
    date_of_manufacture = models.DateField(
        verbose_name=_('Date of Manufacture')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created At')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Last Updated')
    )

    class Meta:
        verbose_name = _('Lab Equipment')
        verbose_name_plural = _('Lab Equipments')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['instrument_id']),
            models.Index(fields=['serial_number']),
        ]

    def __str__(self):
        return f"{self.equipment_name} - {self.instrument_id}"

    def is_calibration_due(self):
        from django.utils import timezone
        return timezone.now().date() >= self.calibration_due_date