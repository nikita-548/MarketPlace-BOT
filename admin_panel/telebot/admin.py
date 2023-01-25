from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Users


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_description", "product_price", "product_quantity", "get_image")

    def get_image(self, obj):
        return mark_safe(f'<img src={{obj.product_image.url}} width="50" height="60">')


admin.site.register(Users)
