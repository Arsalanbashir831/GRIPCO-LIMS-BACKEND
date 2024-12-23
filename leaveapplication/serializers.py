from rest_framework import serializers
from .models import LeaveApplication

class LeaveApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApplication
        fields = "__all__"  # Include all fields in the serializer
