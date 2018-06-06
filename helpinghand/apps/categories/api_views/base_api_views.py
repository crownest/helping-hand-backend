# Third-Party
from rest_framework import viewsets, mixins

# Local Django
from categories.models import Category
from categories.serializers import CategorySerializer, CategoryListSerializer


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        else:
            return CategorySerializer
