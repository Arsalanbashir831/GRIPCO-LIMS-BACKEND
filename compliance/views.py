from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import TestCompliance
from .serializers import TestComplianceSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class TestComplianceViewSet(viewsets.ModelViewSet):
    queryset = TestCompliance.objects.all()
    serializer_class = TestComplianceSerializer
    authentication_classes = [JWTAuthentication]  # Ensure JWT Authentication is used
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users

    def list(self, request, *args, **kwargs):
        # Extract user type from the decoded token
        user_type = getattr(request.user, 'emp_type', None)  # Assuming user_type is stored in the User model
        isCompiled = request.query_params.get("isCompiled", None)  # Get isCompiled from query parameters
        print(f"User Type: {user_type}, isCompiled: {isCompiled}")

        # Start with the base queryset
        queryset = self.queryset

        # Filter by user_type
        if user_type:
            if user_type == "technician":
                queryset = queryset.filter(job_status="technician")
            elif user_type in ["sales", "supervisor"]:
                queryset = queryset
            else:
                return Response(
                    {"error": "Invalid user type provided. Valid options are: 'technician', 'sales', 'supervisor'."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {"error": "User type not found in token."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Filter by isCompiled if provided
        if isCompiled is not None:
            if isCompiled.lower() == "true":
                queryset = queryset.filter(isCompiled=True)  # Assuming is_compiled is a BooleanField
            elif isCompiled.lower() == "false":
                queryset = queryset.filter(isCompiled=False)
            else:
                return Response(
                    {"error": "Invalid isCompiled value. Use 'true' or 'false'."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        # Serialize and return the filtered data
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
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
            {"message": "Job deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
