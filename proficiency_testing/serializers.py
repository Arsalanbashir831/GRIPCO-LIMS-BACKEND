from rest_framework import serializers
from .models import ProficiencyTesting
from test_methods.serializers import TestMethodSerializer

class ProficiencyTestingSerializer(serializers.ModelSerializer):
      test_id = TestMethodSerializer(read_only=True)  # Use the nested serializer
      class Meta:
        model = ProficiencyTesting
        fields = ["schedule_id", "test_id", "test_start", "category", "test_status"]
