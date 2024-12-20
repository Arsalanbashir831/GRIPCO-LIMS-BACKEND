from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .models import ProficiencyTesting
from .serializers import ProficiencyTestingSerializer


class ProficiencyTestingViewSet(viewsets.ModelViewSet):
    queryset = ProficiencyTesting.objects.all()
    serializer_class = ProficiencyTestingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

    @action(detail=False, methods=['get'])
    def filter_by_date(self, request):
        year = request.query_params.get('year', None)
        month = request.query_params.get('month', None)
        queryset = self.queryset

        if year:
            queryset = queryset.filter(test_start__year=year)
        if month:
            queryset = queryset.filter(test_start__month=month)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
