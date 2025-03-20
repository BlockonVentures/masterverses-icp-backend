from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

# Admin: CustomUserAdmin
# ---------------------------------------------------------------------------------------------------------------------------
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("address", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    
    fieldsets = (
        (None, {"fields": ("address", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "address", "is_staff", "is_active", "groups", "user_permissions"
                ),
            },
        ),
    )
    
    search_fields = ("address",)
    ordering = ("address",)

# Admin: Profile
# ---------------------------------------------------------------------------------------------------------------------------
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name"]

def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(User, CustomUserAdmin)
_register(Profile, ProfileAdmin)