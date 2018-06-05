# Third-Party
from rest_framework import viewsets, mixins, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

# Local Django
from needs.models import Need
from needs.serializers import (
    NeedSerializer, NeedListSerializer, NeedCreateSerializer,
    NeedRetrieveSerializer
)


class NeedViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Need.objects.all()
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return NeedListSerializer
        elif self.action == 'create':
            return NeedCreateSerializer
        elif self.action == 'retrieve':
            return NeedRetrieveSerializer
        else:
            return NeedSerializer

    def perform_create(self, serializer):
        serializer.save(
            creator=self.request.user
        )
