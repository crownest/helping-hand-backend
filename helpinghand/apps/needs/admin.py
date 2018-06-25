# Django
from django.contrib import admin
from django.utils.translation import ugettext as _

# Local Django
from needs.models import Need, NeedItem


class NeedItemInline(admin.TabularInline):
    model = NeedItem
    extra = 0
    fields = ('name', 'remaining', 'is_fixed')


@admin.register(Need)
class NeedAdmin(admin.ModelAdmin):
    inlines = (NeedItemInline,)

    fieldsets = (
        (_('Base'), {
            'fields': ('title', 'description', 'is_fixed')
        }),
        (_('Detail'), {
            'fields': (
                'address', 'end_date', 'creator', 'categories', 'supporters', 'lat', 'long'
            )
        }),
        (_('Important dates'), {
            'classes': ('collapse',),
            'fields': ('create_date', 'update_date')
        }),
    )
    readonly_fields = ('create_date', 'update_date')
    filter_horizontal = ('categories', 'supporters')

    list_display = (
        'title', 'end_date', 'is_fixed', 'creator', 'create_date', 'update_date', 'lat', 'long'
    )
    list_filter = (
        'create_date', 'update_date', 'is_fixed', 'categories', 'supporters', 'lat', 'long'
    )
    search_fields = ('title',)


@admin.register(NeedItem)
class NeedItemAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Base'), {
            'fields': ('need', 'name')
        }),
        (_('Detail'), {
            'fields': ('is_fixed', 'remaining')
        }),
        (_('Important dates'), {
            'classes': ('collapse',),
            'fields': ('create_date', 'update_date')
        }),
    )
    readonly_fields = ('create_date', 'update_date')

    list_display = (
        'name', 'remaining', 'need', 'create_date', 'update_date', 'is_fixed'
    )
    list_filter = ('is_fixed', 'create_date', 'update_date')
    search_fields = ('name', 'need__title')
