from django.contrib import admin

from ecommerce import models


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'cylinder_count', 'passenger_count', 'color', 'cylinder_volume', 'owner_name')
    search_fields = ('name', 'color', 'owner_name')
