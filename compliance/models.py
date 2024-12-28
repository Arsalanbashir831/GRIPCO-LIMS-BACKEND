from django.db import models  # Import Django's models


class TestCompliance(models.Model):
    STATUS_TYPES = [
        # ("sales", "Sales"),
        ("supervisor", "Supervisor"),
        ("technician", "Technician"),
        ("complete", "Complete"),
     
    ]

    job_id = models.AutoField(primary_key=True)
    client_data = models.JSONField()
    job_status = models.CharField(
        max_length=20,
        choices=STATUS_TYPES,
        default="supervisor",
    )
    job_data = models.JSONField()
    isCompiled = models.BooleanField(default=False)
    checklist_data = models.JSONField(null=True)
    def __str__(self):
        return f"Job ID: {self.job_id}, Status: {self.job_status}"
