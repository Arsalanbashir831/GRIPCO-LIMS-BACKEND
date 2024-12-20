from django.contrib import admin
from .models import CalibrationList
from unfold.admin import ModelAdmin
@admin.register(CalibrationList)
class CalibrationListAdmin(ModelAdmin):
    list_display = ('instrument_name', 'instrument_id', 'calibrated_by', 'calibration_date', 'calibration_due_date', 'is_calibration_due', 'created_at')
    search_fields = ('instrument__equipment_name', 'instrument__instrument_id', 'calibrated_by', 'calibration_certification_number')
    list_filter = ('calibration_date', 'calibration_due_date', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fields = ['instrument']
    actions = ['mark_as_due_soon']

    def instrument_name(self, obj):
        """
        Display the equipment name of the related instrument.
        """
        return obj.instrument.equipment_name
    instrument_name.short_description = "Equipment Name"

    def instrument_id(self, obj):
        """
        Display the instrument ID of the related instrument.
        """
        return obj.instrument.instrument_id
    instrument_id.short_description = "Instrument ID"

    def is_calibration_due(self, obj):
        """
        Display whether calibration is due.
        """
        return obj.is_calibration_due()
    is_calibration_due.boolean = True
    is_calibration_due.short_description = "Calibration Due"

    def mark_as_due_soon(self, request, queryset):
        """
        Custom action to mark selected calibrations as due soon (for example, if within 30 days).
        """
        from datetime import timedelta
        from django.utils import timezone
        due_soon_date = timezone.now().date() + timedelta(days=30)
        marked_count = queryset.filter(calibration_due_date__lte=due_soon_date).count()
        self.message_user(request, f"{marked_count} calibration(s) marked as due soon.")
    mark_as_due_soon.short_description = "Mark as Due Soon"
