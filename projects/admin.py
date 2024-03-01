from django.contrib import admin
from django.utils.html import mark_safe
from .models import UserProfile, Product, Order, OrderItem, Payment


class OrderItemInline(admin.TabularInline):  
    model = OrderItem
    extra = 1  


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]  
    list_display = ['name', 'price', 'stock', 'image_thumbnail']
    list_filter = ['price', 'stock']
    search_fields = ['name', 'description']

    def image_thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return "No Image"
    image_thumbnail.short_description = 'Image'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]  
    list_display = ['id', 'user', 'order_date', 'status', 'total']
    list_filter = ['status', 'order_date']
    search_fields = ['user__user__username', 'status']  


# Registering the remaining models with the default admin interface
admin.site.register(UserProfile)
admin.site.register(OrderItem)
admin.site.register(Payment)
