from rest_framework import serializers
from .models import TestMethod

class TestMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestMethod
        fields = ['test_id','test_name', 'test_description', 'test_columns']

    def create(self, validated_data):
        print("Creating TestMethod with data:", validated_data)  # Debug log
        return super().create(validated_data)

    def update(self, instance, validated_data):
        print("Updating TestMethod with data:", validated_data)  # Debug log
        return super().update(instance, validated_data)
