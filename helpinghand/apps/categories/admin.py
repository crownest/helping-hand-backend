# Django
from django.contrib import admin

# Local Django
from categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', ('create_date', 'update_date'))
    readonly_fields = ('create_date', 'update_date')

    list_display = ('name', 'create_date', 'update_date')
    search_fields = ('name',)
