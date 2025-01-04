from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestComplianceViewSet ,get_compiled_report,upload_compiled_report

router = DefaultRouter()
router.register(r'test_compliance', TestComplianceViewSet)


urlpatterns = [
     path('<int:job_id>/compiled_report/', get_compiled_report),
    path('upload-report/<int:job_id>/', upload_compiled_report, name='upload_compiled_report'),
    path('', include(router.urls)),
]
