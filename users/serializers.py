from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    profile_picture_url = serializers.SerializerMethodField()  # Add a field for image URL

    class Meta:
        model = User
        fields = '__all__'  # Returns all fields
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},  # Hide password from response
            'username': {'required': False},  # Allow partial updates
        }

    def create(self, validated_data):
        """
        Hash the password before saving a new employee instance.
        """
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        Update the employee instance, ensuring the password is hashed if updated.
        """
        for attr, value in validated_data.items():
            if attr == 'password' and value:  # Only hash password if provided
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    def get_profile_picture_url(self, obj):
        """
        Return the absolute URL of the profile picture.
        """
        if obj.profile_picture:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.profile_picture.url) if request else obj.profile_picture.url
        return None
