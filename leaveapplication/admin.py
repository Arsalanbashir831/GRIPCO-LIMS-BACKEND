from django.contrib import admin
from .models import LeaveApplication
from unfold.admin import ModelAdmin

@admin.register(LeaveApplication)
class LeaveApplicationAdmin(ModelAdmin):
    # Fields to display in the admin list view
    list_display = (
        'user', 
        'creation_date', 
        'start_date', 
        'end_date', 
        'reason', 
        'is_approved'
    )
    
    # Fields to filter by in the admin interface
    list_filter = (
        'is_approved', 
        'creation_date', 
        'start_date', 
        'end_date'
    )
    
    # Fields to search in the admin interface
    search_fields = (
        'user__username', 
        'reason'
    )
    
    # Fields to show in the detail view of the admin interface
   
    # Fields to display as read-only
    readonly_fields = (
        'creation_date',
    )
    
    # Order of fields in the admin list view
    ordering = ('-creation_date',)
