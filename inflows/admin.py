from django.contrib import admin
from .models import Inflow


@admin.register(Inflow)
class InflowAdmin(admin.ModelAdmin):
    list_display = ['supplier', 'product', 'quantity',]
    search_fields = ['supplier', 'product', 'quantity',]
