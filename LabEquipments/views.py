from rest_framework import viewsets
from .models import LabEquipment
from .serializers import LabEquipmentSerializer

class LabEquipmentViewSet(viewsets.ModelViewSet):
    queryset = LabEquipment.objects.all()
    serializer_class = LabEquipmentSerializer
