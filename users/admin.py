from django.contrib import admin
from django.contrib.auth.hashers import make_password
from django.utils.html import format_html
from .models import User
from unfold.admin import ModelAdmin  # Ensure Unfold is installed

@admin.register(User)
class EmployeesAdmin(ModelAdmin):
    fieldsets = (
        ("Basic Information", {
            "fields": ("username", "email", "emp_type", "profile_picture", "is_staff", "password")
        }),
        ("Employment Details", {
            "fields": (
                "employee_id", "gender", "marital_status", "nationality",
                "branch_name", "department", "position", "contract_type",
                "joining_date", "employment_status", "line_manager",
                "contract_duration", "contract_issuance_date", "contract_expiry_date",
                "contracted_hours_per_day"
            )
        }),
        ("Salary & Allowances", {
            "fields": (
                "basic_salary", "house_allowance", "transport_allowance", "food_allowance",
                "other_allowance", "gosi_salary", "total_salary"
            )
        }),
        ("Overtime & Leave", {
            "fields": ("overtime_type", "overtime_hourly_rate", "leave_entitlement")
        }),
        ("GOSI & Identification", {
            "fields": (
                "gosi_number", "saudi_arrival_date", "id_type", "id_number",
                "name_in_id_english", "name_in_id_arabic", "id_issue_date",
                "id_expiry_date", "id_issue_place", "iqama_profession", "id_file"
            )
        }),
        ("Passport Details", {
            "fields": (
                "passport_number", "passport_name", "passport_issue_date",
                "passport_expiry_date", "passport_issue_place", "passport_file"
            )
        }),
        ("Driving License", {
            "fields": (
                "local_driving_license_number", "local_driving_license_expiry",
                "local_driving_license_file"
            )
        }),
        ("Banking Details", {
            "fields": ("bank_name", "account_number", "iban")
        }),
    )

    list_display = (
        "username", "email", "employee_id", "emp_type", "position",
        "branch_name", "basic_salary", "total_salary", "is_staff", "display_profile_picture",
        "display_change_password"
    )
    
    list_filter = ("emp_type", "is_staff", "is_active", "branch_name", "department", "position")
    search_fields = ("username", "email", "employee_id", "branch_name", "department", "position")
    ordering = ("username",)

    actions = ["reset_password"]

    def save_model(self, request, obj, form, change):
        """
        Ensure password is hashed before saving.
        """
        if "password" in form.changed_data:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

    def reset_password(self, request, queryset):
        """
        Reset passwords for selected employees.
        """
        for employee in queryset:
            new_password = "default123"  # Change this for better security
            employee.password = make_password(new_password)
            employee.save()
            self.message_user(
                request,
                f"Password for {employee.username} has been reset to '{new_password}'",
            )

    reset_password.short_description = "Reset password for selected employees"

    def display_change_password(self, obj):
        """
        Display a 'Change Password' link in the list view.
        """
        return format_html(
            '<a href="/admin/auth/user/{}/password/">Change Password</a>', obj.id
        )

    display_change_password.short_description = "Change Password"

    def display_profile_picture(self, obj):
        """
        Display a thumbnail of the profile picture in the admin panel.
        """
        if obj.profile_picture:
            return format_html(
                '<img src="{}" width="40" height="40" style="border-radius:50%;" />', obj.profile_picture.url
            )
        return "No Image"

    display_profile_picture.short_description = "Profile Picture"

