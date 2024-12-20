from rest_framework import  viewsets, routers
from .serializers import CalibrationListSerializer
from .models import CalibrationList


# ViewSets
class CalibrationListViewSet(viewsets.ModelViewSet):
    queryset = CalibrationList.objects.all()
    serializer_class = CalibrationListSerializer
