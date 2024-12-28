from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import CalibrationListSerializer
from .models import CalibrationList

# ViewSets
class CalibrationListViewSet(viewsets.ModelViewSet):
    queryset = CalibrationList.objects.all()
    serializer_class = CalibrationListSerializer

    # Override the destroy method to send a custom message on successful deletion
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the object to be deleted
        self.perform_destroy(instance)  # Perform the deletion
        return Response({"message": "Delete successful"}, status=status.HTTP_204_NO_CONTENT)  # Return a custom message

    def perform_destroy(self, instance):
        # Perform the actual deletion
        instance.delete()
