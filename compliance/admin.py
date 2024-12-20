from django.contrib import admin
from .models import TestCompliance
from unfold.admin import ModelAdmin
@admin.register(TestCompliance)
class TestComplianceAdmin(ModelAdmin):
    list_display = ('job_id', 'job_status', 'get_client_summary', 'get_job_summary')
    search_fields = ('job_status',)
    list_filter = ('job_status',)
    ordering = ('-job_id',)
    readonly_fields = ('job_id',)
    actions = ['mark_as_sales', 'mark_as_supervisor', 'mark_as_technician']

    def get_client_summary(self, obj):
        """
        Custom method to display a summarized view of client_data.
        """
        return str(obj.client_data)[:50] + "..." if len(str(obj.client_data)) > 50 else obj.client_data
    get_client_summary.short_description = "Client Data"

    def get_job_summary(self, obj):
        """
        Custom method to display a summarized view of job_data.
        """
        return str(obj.job_data)[:50] + "..." if len(str(obj.job_data)) > 50 else obj.job_data
    get_job_summary.short_description = "Job Data"

    def mark_as_sales(self, request, queryset):
        """
        Custom action to mark selected jobs as Sales.
        """
        rows_updated = queryset.update(job_status="sales")
        self.message_user(request, f"{rows_updated} job(s) marked as Sales.")
    mark_as_sales.short_description = "Mark selected jobs as Sales"

    def mark_as_supervisor(self, request, queryset):
        """
        Custom action to mark selected jobs as Supervisor.
        """
        rows_updated = queryset.update(job_status="supervisor")
        self.message_user(request, f"{rows_updated} job(s) marked as Supervisor.")
    mark_as_supervisor.short_description = "Mark selected jobs as Supervisor"

    def mark_as_technician(self, request, queryset):
        """
        Custom action to mark selected jobs as Technician.
        """
        rows_updated = queryset.update(job_status="technician")
        self.message_user(request, f"{rows_updated} job(s) marked as Technician.")
    mark_as_technician.short_description = "Mark selected jobs as Technician"
