# Local Django
from .base_api_views import UserViewSet
from users.serializers import (
    UserSerializer, UserCreateSerializerV1, UserUpdateSerializerV1,
    UserPasswordChangeSerializerV1, UserPasswordForgotSerializerV1,
    UserActivationResendSerializerV1,
)


class UserViewSetV1(UserViewSet):

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializerV1
        elif self.action == 'update':
            return UserUpdateSerializerV1
        else:
            return UserSerializer

    def get_route_serializer_class(self):
        if self.action == 'change_password':
            return UserPasswordChangeSerializerV1
        elif self.action == 'forgot_password':
            return UserPasswordForgotSerializerV1
        elif self.action == 'resend_activation':
            return UserActivationResendSerializerV1
        else:
            return UserSerializer
