# Third-Party
from rest_framework import serializers

# Django
from django.utils.translation import ugettext_lazy as _

# Local Django
from needs.models import Need, NeedItem
from users.serializers import UserListSerializer
from categories.serializers import CategoryListSerializer


class NeedSerializer(serializers.ModelSerializer):
    supporters = UserListSerializer(many=True, read_only=True)
    categories = CategoryListSerializer(many=True, read_only=True)

    class Meta:
        model = Need
        fields = ('id', 'title', 'description', 'address',
                  'end_date', 'is_fixed', 'categories', 'supporters'
                  )


class NeedListSerializer(NeedSerializer):
    pass


class NeedCreateSerializer(NeedSerializer):
    class Meta:
        model = Need
        fields = ('id', 'title', 'description', 'address',
                  'end_date', 'is_fixed', 'categories', 'supporters'
                  )


class NeedRetrieveSerializer(NeedSerializer):
    pass


class NeedUpdateSerializer(NeedSerializer):
    class Meta:
        model = Need
        fields = ('id', 'title', 'description', 'address',
                  'end_date', 'is_fixed', 'categories', 'supporters'
                  )

    def validate_date(self, value):
        super(NeedUpdateSerializer, self).validate_date(value)

        if value == self.instance.date:
            raise serializers.ValidationError(_('Can not select same reminder.'))

        return value


class NeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeedItem
        fields = ('id', 'name', 'remaining', 'is_fixed', 'need')


class NeedItemListSerializer(NeedItemSerializer):
    pass


class NeedItemCreateSerializer(NeedItemSerializer):
    class Meta:
        model = NeedItem
        fields = ('id', 'name', 'remaining', 'is_fixed', 'need')
