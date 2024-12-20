from django.contrib import admin
from .models import ProficiencyTesting
from unfold.admin import ModelAdmin
@admin.register(ProficiencyTesting)
class ProficiencyTestingAdmin(ModelAdmin):
    list_display = ('schedule_id', 'test_id', 'test_start', 'category', 'test_status')  # Columns to display
    search_fields = ('test_id__test_name', 'category', 'test_status')  # Searchable fields
    list_filter = ('category', 'test_status', 'test_start')  # Filters for the sidebar
    ordering = ('-test_start',)  # Default ordering
    actions = ['mark_as_completed']  # Custom actions

    autocomplete_fields = ['test_id']  # For better performance when there are many TestMethod entries

    def mark_as_completed(self, request, queryset):
        """
        Custom admin action to mark selected tests as completed.
        """
        rows_updated = queryset.update(test_status='completed')
        self.message_user(
            request, f"{rows_updated} test(s) marked as completed successfully."
        )
    mark_as_completed.short_description = "Mark selected tests as completed"

    def test_id_name(self, obj):
        """
        Display the name of the related TestMethod instead of the ID.
        """
        return obj.test_id.test_name
    test_id_name.short_description = "Test Name"
