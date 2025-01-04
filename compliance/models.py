from django.db import models

class TestCompliance(models.Model):
    STATUS_TYPES = [
        ("supervisor", "Supervisor"),
        ("technician", "Technician"),
        ("pending approval", "Pending Approval"),
        ("Approved", "Approved"),
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

    # Fixed File Upload Field
    compiled_report = models.FileField(upload_to='test_reports/', blank=True, null=True)

    def __str__(self):
        return f"Job ID: {self.job_id}, Status: {self.job_status}"
