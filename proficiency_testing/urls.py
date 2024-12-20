from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProficiencyTestingViewSet

router = DefaultRouter()
router.register(r'proficiency_testing', ProficiencyTestingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
