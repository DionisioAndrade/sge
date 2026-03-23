from django.contrib import admin
from products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'category',]
    search_fields = ['title', 'brand', 'category',]
