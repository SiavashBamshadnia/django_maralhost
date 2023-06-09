from django.contrib.auth import admin as auth_admin
from django.contrib import admin

from accounts import models


@admin.register(models.User)
class UserAdmin(auth_admin.UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )
