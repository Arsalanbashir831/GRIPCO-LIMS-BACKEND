from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import LabEquipment
from .serializers import LabEquipmentSerializer, LabEquipmentListSerializer

class LabEquipmentViewSet(viewsets.ModelViewSet):
    """
    Viewset for LabEquipment with multiple filtering and custom actions.
    """
    queryset = LabEquipment.objects.all()
    serializer_class = LabEquipmentSerializer
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    ]
    
    # Filterable fields
    filterset_fields = [
        'manufacturer_name', 
        'calibration_due_date', 
        'equipment_name'
    ]
    
    # Searchable fields
    search_fields = [
        'equipment_name', 
        'manufacturer_name', 
        'instrument_id', 
        'serial_number'
    ]
    
    # Orderable fields
    ordering_fields = [
        'calibration_due_date', 
        'date_of_manufacture', 
        'created_at'
    ]

    def get_serializer_class(self):
        """
        Use different serializers for list and retrieve actions.
        """
        if self.action == 'list':
            return LabEquipmentListSerializer
        return LabEquipmentSerializer

    @action(detail=False, methods=['GET'])
    def calibration_due(self, request):
        """
        Custom action to retrieve equipment due for calibration.
        """
        from django.utils import timezone
        
        current_date = timezone.now().date()
        due_equipment = LabEquipment.objects.filter(
            calibration_due_date__lte=current_date
        )
        
        serializer = self.get_serializer(due_equipment, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def update_calibration(self, request, pk=None):
        """
        Custom action to update calibration details for a specific equipment.
        """
        instance = self.get_object()
        serializer = self.get_serializer_class()(
            instance, 
            data=request.data, 
            partial=True
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)