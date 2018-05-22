# Django
from django.contrib import admin

# Local Django
from needs.models import Need, NeedItem


class NeedItemInline(admin.StackedInline):
    model = NeedItem
    fields = ('name', 'is_fixed')


@admin.register(Need)
class NeedAdmin(admin.ModelAdmin):
    inlines = (NeedItemInline,)

    fields = (
        'title', 'description', 'address', 'end_date',
        'is_fixed', 'creator', 'supporters'
    )

    list_display = (
        'title', 'description', 'address', 'end_date',
        'is_fixed', 'creator', 'create_date', 'update_date'
    )
    search_fields = ('title', 'address')


@admin.register(NeedItem)
class NeedItemAdmin(admin.ModelAdmin):
    fields = ('name', 'need', 'is_fixed')

    list_display = ('name', 'need', 'create_date', 'update_date', 'is_fixed')
    search_fields = ('name',)
