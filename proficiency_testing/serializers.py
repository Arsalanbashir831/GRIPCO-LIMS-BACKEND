from rest_framework import serializers
from .models import ProficiencyTesting


class ProficiencyTestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProficiencyTesting
        fields = ["schedule_id", "test_id", "test_start", "category", "test_status"]
