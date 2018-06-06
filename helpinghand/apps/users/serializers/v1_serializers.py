# Local Django
from .base_serializers import (
    UserCreateSerializer, UserListSerializer, UserUpdateSerializer, UserPasswordChangeSerializer,
    UserPasswordForgotSerializer, UserActivationResendSerializer
)


class UserListSerializerV1(UserListSerializer):
    pass


class UserCreateSerializerV1(UserCreateSerializer):
    pass


class UserUpdateSerializerV1(UserUpdateSerializer):
    pass


class UserPasswordChangeSerializerV1(UserPasswordChangeSerializer):
    pass


class UserPasswordForgotSerializerV1(UserPasswordForgotSerializer):
    pass


class UserActivationResendSerializerV1(UserActivationResendSerializer):
    pass
