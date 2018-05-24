# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin
from django.utils.translation import ugettext as _

# Local Django
from users.models import User


@admin.register(User)
class UserAdmin(_UserAdmin):
    fieldsets = (
        (_('Base'), {
            'fields': ('email', 'password')
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name')
        }),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_verified',
                'is_superuser', 'groups', 'user_permissions'
            )
        }),
        (_('Important dates'), {
            'classes': ('collapse',),
            'fields': ('last_login', 'create_date', 'update_date')
        }),
    )
    readonly_fields = ('last_login', 'create_date', 'update_date')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'last_name',
                'password1', 'password2'
            )
        }),
    )

    list_display = (
        'first_name', 'last_name', 'email',
        'is_active', 'is_verified', 'is_superuser'
    )
    list_filter = ('is_active', 'is_verified', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('first_name', 'last_name')
