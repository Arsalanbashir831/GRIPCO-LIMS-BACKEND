from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User
from unfold.admin import ModelAdmin

@admin.register(User)
class UserAdmin(ModelAdmin):
    fieldsets = DefaultUserAdmin.fieldsets + (
        (None, {'fields': ('emp_type', 'profile_picture')}),
    )
    list_display = ['username', 'email', 'emp_type', 'is_staff']
    list_filter = ['emp_type', 'is_staff', 'is_active']
