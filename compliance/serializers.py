from rest_framework import serializers
from .models import TestCompliance


class TestComplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCompliance
        fields = [
            "job_id",
            "client_data",
            "job_status",
            "job_data",
            'isCompiled'
        ]
