from django.contrib import admin
from . import models


class OrderItemsInline(admin.TabularInline):
    model = models.OrderItems
    extra = 0
    readonly_fields = ['product', 'price', 'quantity',]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False


class TableAdmin(admin.ModelAdmin):
    list_display = ['table_no', 'seat', 'fill']
    list_filter = ['seat', 'fill']
    search_fields = ['table_no']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'type', 'category']
    list_filter = ['type', 'category', 'price']
    search_fields = ['name',]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    ordering = ['name',]
    search_fields = ['name', 'email', 'phone']


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['customer', 'payment_method', 'table_no', 'peoples', 'total', 'waiter']
    list_display = ['cus_name', 'table_no', 'date_time', 'total']
    inlines = [OrderItemsInline,]
    list_filter = ['date_time', 'table_no', 'peoples', 'total', 'waiter']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


class WaiterAdmin(admin.ModelAdmin):
    search_fields = ['name']


class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount']
    list_filter = ['discount']
    search_fields = ['code']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['code', 'discount']
        else:
            return []


admin.site.register(models.Table, TableAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Waiter, WaiterAdmin)
admin.site.register(models.PromoCode, PromoCodeAdmin)