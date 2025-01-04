from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import TestCompliance
from .serializers import TestComplianceSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, FileResponse, JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes,parser_classes
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authentication import TokenAuthentication

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
        
        
@api_view(['GET'])
def get_compiled_report(request, job_id):
    job = get_object_or_404(TestCompliance, job_id=job_id)

    if job.compiled_report:
        file_path = job.compiled_report.path  # Full path to the file
        file_url = job.compiled_report.url    # URL accessible via MEDIA_URL

        # Return the file URL
        return JsonResponse({"file_url": file_url}, status=200)

    return Response({"error": "No compiled report available for this job."}, status=404)

@api_view(['PUT'])
@parser_classes([MultiPartParser, FormParser])  # Allow file uploads
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated])
def upload_compiled_report(request, job_id):
    """
    API endpoint to upload a compiled report (PDF) for a given job_id.
    """
    try:
        job = get_object_or_404(TestCompliance, job_id=job_id)

        # Ensure a file is provided
        if 'compiled_report' not in request.FILES:
            return Response({"error": "No file uploaded."}, status=status.HTTP_400_BAD_REQUEST)

        file = request.FILES['compiled_report']

        # Validate file type (Only allow PDFs)
        if not file.name.endswith('.pdf'):
            return Response({"error": "Only PDF files are allowed."}, status=status.HTTP_400_BAD_REQUEST)

        # Save the file directly to the model field
        job.compiled_report = file
        job.save()

        # Return success response with file URL
        return Response(
            {"message": "File uploaded successfully!", "file_url": job.compiled_report.url},
            status=status.HTTP_200_OK
        )

    except Exception as e:
        error_trace = traceback.format_exc()
        print("Error:", error_trace)  # Log to terminal
        return Response({"error": str(e), "trace": error_trace}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)