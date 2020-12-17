from django.contrib import admin
from .models import Supplier, Item


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'date')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price')


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Item, ItemAdmin)
