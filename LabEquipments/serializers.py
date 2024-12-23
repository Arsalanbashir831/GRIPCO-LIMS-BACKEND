from rest_framework import serializers
from .models import LabEquipment

class LabEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabEquipment
        fields = "__all__"  # Include all fields in the serializer
