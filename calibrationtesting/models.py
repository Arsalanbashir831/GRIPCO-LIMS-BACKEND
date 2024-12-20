from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from LabEquipments.models import LabEquipment
class CalibrationList(models.Model):
    instrument = models.ForeignKey(
        LabEquipment,
        on_delete=models.CASCADE,
        related_name='calibrations',
        verbose_name=_('instrument_id')
    )
    calibrated_by = models.CharField(
        max_length=150,
        verbose_name=_('Calibrated By')
    )
    calibration_certification_number = models.CharField(
        max_length=100,
        verbose_name=_('Calibration Certification Number')
    )
    calibration_date = models.DateField(
        verbose_name=_('Calibration Date')
    )
    calibration_due_date = models.DateField(
        verbose_name=_('Calibration Due Date')
    )
    remarks = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Remarks')
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
        verbose_name = _('Calibration Record')
        verbose_name_plural = _('Calibration Records')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['instrument']),
            models.Index(fields=['calibration_due_date']),
        ]

    def __str__(self):
        return f"{self.instrument.equipment_name} - {self.instrument.instrument_id}"

    def is_calibration_due(self):
        from django.utils import timezone
        return timezone.now().date() >= self.calibration_due_date