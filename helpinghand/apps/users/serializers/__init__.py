# Local Django
from .base_serializers import (
    UserSerializer, UserListSerializer, UserCreateSerializer, UserUpdateSerializer,
    UserPasswordChangeSerializer, UserPasswordForgotSerializer,
    UserActivationResendSerializer,
)

from .v1_serializers import (
    UserCreateSerializerV1, UserListSerializerV1, UserUpdateSerializerV1, UserPasswordChangeSerializerV1,
    UserPasswordForgotSerializerV1, UserActivationResendSerializerV1,
)
