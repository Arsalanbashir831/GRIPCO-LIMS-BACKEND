from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = [ 'user', 'reporting_time', 'checkout_time', 'working_hours', 'overtime_hours', 'is_approved', 'creation_date']
        read_only_fields = ['user',  'creation_date']  # 'user' and 'schedule_id' are read-only
