from django.contrib import admin

from core.models import User, UserProfile

from shared.base_admin import BaseModelAdmin


@admin.register(User)
class UserAdmin(BaseModelAdmin):
    model = User
    list_display = ["uid", "email", "last_login"]

    fieldsets = (
        (None, {"fields": ("email", "password", "new_password")}),
        (
            "Other",
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "phone",
                    "uid",
                    "last_login",
                    "status",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )

    list_filter = [
        "status",
        "last_login",
    ]

    search_fields = ("phone", "email")
    readonly_fields = BaseModelAdmin.readonly_fields + [
        "last_login",
    ]
    list_select_related = True
    show_full_result_count = False
    ordering = ("-created_at",)


@admin.register(UserProfile)
class UserProfileAdmin(BaseModelAdmin):
    model = UserProfile
    list_display = [
        "user",
        "photo",
        "bio",
        "date_of_birth",
        "gender",
    ]
