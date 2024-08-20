from rest_framework import serializers
from portal.models import User  # Adjust the import according to your project structure

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'status']
