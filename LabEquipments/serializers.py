from rest_framework import serializers
from .models import LabEquipment

class LabEquipmentSerializer(serializers.ModelSerializer):
    """
    Serializer for LabEquipment model with all fields.
    """
    class Meta:
        model = LabEquipment
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def validate_calibration_due_date(self, value):
        """
        Custom validation to ensure calibration due date is after calibration date.
        """
        if value and self.initial_data.get('calibration_date'):
            calibration_date = serializers.DateField().to_internal_value(
                self.initial_data.get('calibration_date')
            )
            if value <= calibration_date:
                raise serializers.ValidationError(
                    "Calibration due date must be after the calibration date."
                )
        return value

class LabEquipmentListSerializer(serializers.ModelSerializer):
    """
    Simplified serializer for list views with key information.
    """
    class Meta:
        model = LabEquipment
        fields = [
            'list_id', 
            'instrument_id', 
            'equipment_name', 
            'manufacturer_name', 
            'calibration_due_date', 
            'is_calibration_due'
        ]
        read_only_fields = fields

    is_calibration_due = serializers.SerializerMethodField()

    def get_is_calibration_due(self, obj):
        return obj.is_calibration_due()