from django.contrib import admin
from .models import TestMethod
from unfold.admin import ModelAdmin

@admin.register(TestMethod)
class TestMethodAdmin(ModelAdmin):
    list_display = ('test_id', 'test_name', 'test_description')  # Columns to display in the list view
    search_fields = ('test_name', 'test_description')  # Searchable fields
    list_filter = ('test_name',)  # Filters for the sidebar
    ordering = ('test_id',)  # Default ordering
    actions = ['duplicate_test_method']  # Custom actions

    def duplicate_test_method(self, request, queryset):
        """
        Custom admin action to duplicate selected test methods.
        """
        for obj in queryset:
            obj.pk = None  # Reset primary key to create a new object
            obj.test_name = f"{obj.test_name} (Copy)"  # Append 'Copy' to the name to avoid conflicts
            obj.save()

        self.message_user(request, f"{queryset.count()} TestMethod(s) duplicated successfully.")
    duplicate_test_method.short_description = "Duplicate selected Test Methods"
