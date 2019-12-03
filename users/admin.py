from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import MyUser


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ('email', 'phone', 'is_active', 'is_superuser')
    search_fields = ('email', 'phone')
    readonly_fields = ('date_joined',)
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'real_name', 'phone')}),
        ('Permissions', {
            'fields': ('is_active', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'phone', 'password1', 'password2'),
        }),
    )
