# Third-Party
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import detail_route, list_route

# Local Django
from users.models import User
from helpinghand.modules import ActivationKeyModule, MailModule, ResetPasswordKeyModule
from users.serializers import (
    UserPasswordChangeSerializer, UserPasswordForgotSerializer, UserActivationResendSerializer,
    UserSerializer,
)


class UserViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()

    def perform_create(self, serializer):
        # Create User
        user = serializer.save()
        user.set_password(serializer.validated_data.get('password', ''))
        user.save()

        # Create Activation Key
        activation_key = ActivationKeyModule.create_key(user=user)

        # Send Activation Mail
        MailModule.send_activation_mail(activation_key)

        return user

    def get_permissions(self):
        permissions = super(UserViewSet, self).get_permissions()

        if self.action in ['create', 'forgot_password', 'resend_activation']:
            return []

        return permissions

    def get_route_serializer_class(self):
        if self.action == 'change_password':
            return UserPasswordChangeSerializer
        elif self.action == 'forgot_password':
            return UserPasswordForgotSerializer
        elif self.action == 'resend_activation':
            return UserActivationResendSerializer
        else:
            return UserSerializer

    @detail_route(methods=['post'], url_path='password/change',
                  url_name='change-password')
    def change_password(self, request, pk=None):
        user = self.get_object()
        serializer_class = self.get_route_serializer_class()
        serializer = serializer_class(
            data=request.data, context={'user': user}
        )

        if serializer.is_valid():
            user.set_password(serializer.validated_data['new_password'])
            user.save()

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['post'], url_path='password/forgot',
                url_name='forgot-password')
    def forgot_password(self, request):
        serializer_class = self.get_route_serializer_class()
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            # Create Forgot Password Key
            reset_password_key = ResetPasswordKeyModule.create_key(user=serializer.user)

            # Send Forgot Password Mail
            MailModule.send_forgot_password_mail(reset_password_key)

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['post'], url_path='activation/resend',
                url_name='resend-activation')
    def resend_activation(self, request):
        serializer_class = self.get_route_serializer_class()
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            # Create Activation Key
            activation_key = ActivationKeyModule.create_key(user=serializer.user)

            # Send Activation Mail
            MailModule.send_activation_mail(activation_key)

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
