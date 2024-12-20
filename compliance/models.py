from django.db import models  # Import Django's models


class TestCompliance(models.Model):
    STATUS_TYPES = [
        ("sales", "Sales"),
        ("supervisor", "Supervisor"),
        ("technician", "Technician"),
    ]

    job_id = models.AutoField(primary_key=True)
    client_data = models.JSONField()
    job_status = models.CharField(
        max_length=20,
        choices=STATUS_TYPES,
        default="sales",
    )
    job_data = models.JSONField()

    def __str__(self):
        return f"Job ID: {self.job_id}, Status: {self.job_status}"