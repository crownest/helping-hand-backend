# Third-Party
from rest_framework import serializers

# Local Django
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name',
            'is_active', 'is_verified'
        )


class UserListSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')
