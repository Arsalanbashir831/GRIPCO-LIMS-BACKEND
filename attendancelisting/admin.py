from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'creation_date', 'reporting_time', 'checkout_time', 'working_hours', 'overtime_hours')
    search_fields = ('user__username', 'creation_date')
    list_filter = ('creation_date',)
    ordering = ('-creation_date',)
