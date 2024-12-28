from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import LeaveApplication
from .serializers import LeaveApplicationSerializer

class LeaveApplicationViewSet(viewsets.ModelViewSet):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can create/update

    def perform_create(self, serializer):
        """
        Override the perform_create method to automatically associate the logged-in user.
        """
        user = self.request.user  # Get the user from the request
        serializer.save(user=user)  # Save the leave application with the associated user

    def perform_update(self, serializer):
        """
        Override the perform_update method to automatically associate the logged-in user when updating.
        """
        user = self.request.user  # Get the user from the request
        serializer.save(user=user)  # Ensure the user is associated even when updating
