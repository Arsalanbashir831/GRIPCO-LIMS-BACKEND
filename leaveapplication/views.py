from rest_framework import viewsets
from .models import LeaveApplication
from .serializers import LeaveApplicationSerializer

class LeaveApplicationViewSet(viewsets.ModelViewSet):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer

    def perform_create(self, serializer):
        # Automatically associate the logged-in user with the leave application
        serializer.save(user=self.request.user)
