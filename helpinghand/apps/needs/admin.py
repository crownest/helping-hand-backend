# Django
from django.contrib import admin

# Local Django
from needs.models import Need


@admin.register(Need)
class NeedAdmin(admin.ModelAdmin):
    fields = (
        'title', 'description', 'address', 'end_date',
        'is_fixed', 'creator', 'supporters'
    )

    list_display = (
        'title', 'description', 'address', 'end_date',
        'is_fixed', 'creator', 'create_date', 'update_date'
    )
    search_fields = ('title', 'address',)
