from django.contrib import admin
from userAuth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ["id","email", "username","first_name", "last_name","is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("User Credential", {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["first_name","last_name","username"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email","username", "first_name","last_name", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email","username"]
    ordering = ["email","username","id"]
    filter_horizontal = []


# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)
