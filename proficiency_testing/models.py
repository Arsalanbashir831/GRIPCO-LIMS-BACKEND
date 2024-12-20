from django.db import models
from test_methods.models import TestMethod  # Import the TestMethod model directly

class ProficiencyTesting(models.Model):
    CATEGORY_CHOICES = [
        ('GPT', 'Global PT Provider'),
        ('DM', 'Deep Metallurgy PT Provider'),
    ]
    TEST_STATUS = [
        ('pending', 'pending'),
        ('completed', 'completed'),
    ]

    schedule_id = models.AutoField(primary_key=True)
    test_id = models.ForeignKey(TestMethod, on_delete=models.CASCADE) 
    test_start = models.DateField()
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='GPT',
    )
    test_status = models.CharField(
        max_length=50,
        choices=TEST_STATUS,
        default='pending',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['test_id', 'test_start'],
                name='unique_test_per_date'
            )
        ]

    def __str__(self):
        return f"{self.test_id.test_name} - {self.category} on {self.test_start}"
