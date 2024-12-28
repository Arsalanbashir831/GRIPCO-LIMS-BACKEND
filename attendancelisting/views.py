from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .models import Attendance
from .serializers import AttendanceSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically associate the user from the token with the attendance record
        user = self.request.user  # Get the user from the request (authenticated user)
        serializer.save(user=user)  # Save the attendance record with the user

    @action(detail=False, methods=['get'])
    def user_attendance(self, request):
        """
        Custom action to get attendance records for the authenticated user.
        """
        user = request.user
        user_attendance = Attendance.objects.filter(user=user)
        serializer = self.get_serializer(user_attendance, many=True)
        return Response(serializer.data)
