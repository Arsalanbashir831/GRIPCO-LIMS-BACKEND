from rest_framework import serializers

from .models import CalibrationList

# Serializers
class CalibrationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalibrationList
        fields = '__all__'
