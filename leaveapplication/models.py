from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class LeaveApplication(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='leave_records',
        verbose_name=_('User')
    )
    creation_date = models.DateField(
        auto_now_add=True,
        verbose_name=_('Creation Date')
    )
    reason = models.TextField()   
    isApproved = models.BooleanField(default=False)

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