from rest_framework import viewsets
from .models import TestMethod
from .serializers import TestMethodSerializer

class TestMethodViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting TestMethod instances.
    """
    queryset = TestMethod.objects.all()
    serializer_class = TestMethodSerializer
