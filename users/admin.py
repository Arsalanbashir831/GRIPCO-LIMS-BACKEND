from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User
from unfold.admin import ModelAdmin

@admin.register(User)
class UserAdmin(ModelAdmin):
    fields = ['username', 'email', 'emp_type', 'profile_picture', 'is_staff']
    list_display = ['username', 'email', 'emp_type', 'is_staff']
    list_filter = ['emp_type', 'is_staff', 'is_active']
