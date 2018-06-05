# Third-Party
from rest_framework import serializers

# Django
from django.utils.translation import ugettext_lazy as _

# Local Django
from needs.models import Need


class NeedSerializer(serializers.ModelSerializer):

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
