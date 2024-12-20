from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestMethodViewSet

router = DefaultRouter()
router.register(r'testmethods', TestMethodViewSet, basename='testmethod')

urlpatterns = [
    path('', include(router.urls)),  
]
