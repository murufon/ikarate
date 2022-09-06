from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import TwitterAuthToken, TwitterUser

# Register your models here.
User = get_user_model()

@admin.register(User)
class AdminUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        # (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("username", "twitter_screen_name", "is_staff")
    search_fields = ("username",)
    def twitter_screen_name(self, obj):
        return obj.twitter_user.screen_name
    twitter_screen_name.short_description = 'Twitter ID'
    twitter_screen_name.admin_order_field = 'twitter_user__screen_name'

admin.site.register(TwitterAuthToken)
admin.site.register(TwitterUser)