# Local Django
from .base_api_views import CategoryViewSet
from categories.serializers import (
    CategorySerializer, CategoryListSerializer, CategoryListSerializerV1
)


class CategoryViewSetV1(CategoryViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializerV1
        else:
            return CategorySerializer
