# Third-Party
from rest_framework import viewsets, mixins

# Local Django
from needs.models import Need
from needs.serializers import (
    NeedSerializer, NeedListSerializer
)


class NeedViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Need.objects.all()

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return NeedListSerializer
