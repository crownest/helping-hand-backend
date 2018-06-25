# Django
from django.contrib import admin

# Local Django
from categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', ('create_date', 'update_date'))
    readonly_fields = ('create_date', 'update_date')

    list_display = ('name', 'create_date', 'update_date')
    list_filter = ('create_date', 'update_date')
    search_fields = ('name',)

    def get_fields(self, request, *args, **kwargs):
        fields = super(CategoryAdmin, self).get_fields(request, *args, **kwargs)
        exclude_fields = []

        if 'add' in request.path.split('/'):
            exclude_fields += [('create_date', 'update_date')]

        return [field for field in fields if field not in exclude_fields]
