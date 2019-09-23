from django.contrib import admin
from webapp.models import Good


class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'category', 'stock', 'price']
    list_filter = ['name', 'category']
    list_display_links = ['name']
    search_fields = ['name']
    fields = ['name', 'description', 'category', 'stock', 'price']


admin.site.register(Good, GoodAdmin)