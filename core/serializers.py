from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)  # Display username instead of user ID

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'updated_at']
        read_only_fields = ['created_by', 'created_at', 'updated_at']  # Make these fields read-only


class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()  # Display client name instead of client ID
    users = UserSerializer(many=True)  # Use nested serializer to display user details
    created_by = serializers.StringRelatedField(read_only=True)  # Display username instead of user ID

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']
        read_only_fields = ['client', 'created_by', 'created_at']  # Make these fields read-only


class CreateProjectSerializer(serializers.ModelSerializer):
    """Serializer for creating a project with client ID and user IDs."""
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users']
