from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import TestMethod
from .serializers import TestMethodSerializer

class TestMethodViewSet(viewsets.ModelViewSet):
    queryset = TestMethod.objects.all()
    serializer_class = TestMethodSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            print("Validated Data:", serializer.validated_data)  # Debug log
            instance = serializer.save()
            print("Instance Created:", instance)  # Debug log
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)