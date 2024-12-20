from rest_framework import serializers
from .models import TestMethod

class TestMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestMethod
        fields = ['test_id', 'test_name', 'test_description', 'test_columns']  # Include all fields
