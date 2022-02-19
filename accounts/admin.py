from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


User = get_user_model()


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('deviceID', 'password', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('deviceID', 'password1', 'password2')
            }
        ),
    )

    list_display = ('deviceID', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('deviceID',)
    ordering = ('deviceID',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)
