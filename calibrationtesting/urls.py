from rest_framework import serializers, routers
from .views import CalibrationListViewSet
from django.urls import path, include

# Router
router = routers.DefaultRouter()
router.register(r'calibrations', CalibrationListViewSet)

# URL Configuration
urlpatterns = [
    path('', include(router.urls)),
]