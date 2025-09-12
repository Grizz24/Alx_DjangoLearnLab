from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields visible in the admin list
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active", "date_of_birth")

    # Fields grouped in admin detail view
    fieldsets = (
    *UserAdmin.fieldsets,
    (None, {"fields": ("date_of_birth", "profile_photo")}),
)

    # Fields used when creating a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
