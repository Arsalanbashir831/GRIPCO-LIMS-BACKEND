from rest_framework import serializers
from .models import ProficiencyTesting
from test_methods.models import TestMethod

class ProficiencyTestingSerializer(serializers.ModelSerializer):
    # Use PrimaryKeyRelatedField to handle foreign key as an integer (test_id)
    test_id = serializers.PrimaryKeyRelatedField(queryset=TestMethod.objects.all())

    class Meta:
        model = ProficiencyTesting
        fields = ['schedule_id', 'test_id', 'test_start', 'category', 'test_status']

    def to_representation(self, instance):
        # Overriding to return the nested TestMethod data in GET responses
        representation = super().to_representation(instance)
        # Replace test_id with the full TestMethod details in GET responses
        representation['test_id'] = {
            'test_id': instance.test_id.test_id,
            'test_name': instance.test_id.test_name,
            'test_description': instance.test_id.test_description,
            'test_columns': instance.test_id.test_columns,
        }
        return representation
