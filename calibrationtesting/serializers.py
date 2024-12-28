from rest_framework import serializers
from .models import CalibrationList
from LabEquipments.models import LabEquipment

class CalibrationListSerializer(serializers.ModelSerializer):
    # Corrected the source to reference the instrument field
    instrument_name = serializers.CharField(source='instrument.equipment_name', read_only=True)

    class Meta:
        model = CalibrationList
        fields = '__all__'
