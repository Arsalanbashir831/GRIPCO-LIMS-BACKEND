from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _


class Attendance(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='attendance_records',
        verbose_name=_('User')
    )
    creation_date = models.DateField(
        auto_now_add=True,
        verbose_name=_('Creation Date')
    )
    reporting_time = models.TimeField(
        verbose_name=_('Reporting Time')
    )
    checkout_time = models.TimeField(
        blank=True,
        null=True,
        verbose_name=_('Checkout Time')
    )
    working_hours = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
        verbose_name=_('Working Hours')
    )
    overtime_hours = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
        verbose_name=_('Overtime Hours')
    )

    class Meta:
        verbose_name = _('Attendance Record')
        verbose_name_plural = _('Attendance Records')
        ordering = ['-creation_date']
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['creation_date']),
        ]

    def __str__(self):
        return f"Attendance for {self.user.username} on {self.creation_date}"
