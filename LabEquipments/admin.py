from django.contrib import admin
from .models import LabEquipment
from unfold.admin import ModelAdmin
@admin.register(LabEquipment)
class LabEquipmentAdmin(ModelAdmin):
    list_display = ('list_id', 'instrument_id', 'equipment_name', 'manufacturer_name', 'model_name', 'serial_number', 'date_of_manufacture', 'created_at', 'updated_at')
    search_fields = ('instrument_id', 'equipment_name', 'manufacturer_name', 'model_name', 'serial_number')
    list_filter = ('manufacturer_name', 'model_name', 'date_of_manufacture', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    actions = ['mark_as_outdated']

    def mark_as_outdated(self, request, queryset):
        """
        Custom admin action to flag outdated equipment.
        """
        outdated_items = queryset.filter(date_of_manufacture__lt='2000-01-01')  # Example condition
        self.message_user(
            request, f"{outdated_items.count()} equipment item(s) flagged as outdated."
        )
    mark_as_outdated.short_description = "Flag selected items as outdated"
