from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class LeaveApplication(models.Model):
    # Choices for the leave approval status
    APPROVAL_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

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
    start_date = models.DateField(
        verbose_name=_('Start Date')
    )
    end_date = models.DateField(
        verbose_name=_('End Date')
    )
    reason = models.TextField(verbose_name=_('Reason'))   
    is_approved = models.CharField(
        max_length=10,
        choices=APPROVAL_CHOICES,
        default='pending',
        verbose_name=_('Approval Status')
    )

    class Meta:
        verbose_name = _('Leave Application')
        verbose_name_plural = _('Leave Applications')
        ordering = ['-creation_date']
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['creation_date']),
        ]

    def __str__(self):
        return f"Leave Application for {self.user.username} from {self.start_date} to {self.end_date}"
