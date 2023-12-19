from rest_framework import serializers
from django.contrib.auth import get_user_model

class CustomUserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('custom_username', 'custom_password')  # Add other fields as needed
        extra_kwargs = {'custom_password': {'write_only': True}}
