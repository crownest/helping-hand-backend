# Third-Party
from rest_framework import serializers

# Local Django
from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class CategoryListSerializer(CategorySerializer):
    pass
