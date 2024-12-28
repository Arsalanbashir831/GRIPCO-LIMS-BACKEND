from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models import User
from unfold.admin import ModelAdmin
from django.utils.html import format_html

@admin.register(User)
class UserAdmin(ModelAdmin):
    fields = ['username', 'email', 'emp_type', 'profile_picture', 'is_staff', 'password']
    list_display = ['username', 'email', 'emp_type', 'is_staff', 'display_change_password']
    list_filter = ['emp_type', 'is_staff', 'is_active']
    actions = ['reset_password']

    def save_model(self, request, obj, form, change):
        # Hash the password if it's being set or changed
        if 'password' in form.changed_data:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

    def reset_password(self, request, queryset):
        """
        Action to reset passwords for selected users.
        """
        for user in queryset:
            new_password = "default123"  # You can generate a secure password here
            user.password = make_password(new_password)
            user.save()
            self.message_user(
                request,
                f"Password for {user.username} has been reset to '{new_password}'",
            )

    reset_password.short_description = "Reset password for selected users"

    def display_change_password(self, obj):
        """
        Display a 'Change Password' link in the list view for each user.
        """
        return format_html(
            '<a href="/admin/auth/user/{}/password/">Change Password</a>', obj.id
        )

    display_change_password.short_description = "Change Password"
