from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestComplianceViewSet

router = DefaultRouter()
router.register(r'test_compliance', TestComplianceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
