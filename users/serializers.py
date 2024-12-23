from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'emp_type', 'profile_picture']
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},  # Password is write-only and optional for updates
            'username': {'required': False},  # Username is optional for updates
        }

    def create(self, validated_data):
        """
        Hash the password before saving a new user instance.
        """
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        Update the user instance, ensuring the password is hashed if updated.
        """
        for attr, value in validated_data.items():
            if attr == 'password' and value:  # Handle password update, only if provided
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
