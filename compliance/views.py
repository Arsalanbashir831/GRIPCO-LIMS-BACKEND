from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import TestCompliance
from .serializers import TestComplianceSerializer


class TestComplianceViewSet(viewsets.ModelViewSet):

    queryset = TestCompliance.objects.all()
    serializer_class = TestComplianceSerializer

    def list(self, request, *args, **kwargs):
        user_type = request.data.get("user_type", None)  
        if user_type:
            if user_type == "sales":
                queryset = self.queryset.filter(job_status="sales")
            elif user_type == "supervisor":
                queryset = self.queryset.filter(job_status="supervisor")
            elif user_type == "technician":
                queryset = self.queryset.filter(job_status="technician")
            else:
                return Response(
                    {"error": "Invalid user type provided."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            queryset = self.queryset
            
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(
            {"message": "TestCompliance instance deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
