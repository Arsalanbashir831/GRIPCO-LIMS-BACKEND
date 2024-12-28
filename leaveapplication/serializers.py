from rest_framework import serializers
from .models import LeaveApplication

class LeaveApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApplication
        fields = [ 'creation_date', 'start_date', 'end_date', 'reason', 'is_approved']
     
