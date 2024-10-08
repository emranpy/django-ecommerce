from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'username',
        'email',  # Include email in the list_display
        'last_login',
        'date_joined',  # Fix the typo here
        'is_active',
    ]
    readonly_fields = [
        'last_login',
        'date_joined',  # Fix the typo here
    ]
    list_display_links = ("first_name", "last_name", "username")
    ordering = ('-date_joined',)  # Fix the typo here
    
    filter_horizontal = ()
    list_filter = ()
    
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'first_name', 'last_name', 'phone_number', 'password')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_admin', 'is_superadmin')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined'),  # Fix the typo here
        }),
    )

admin.site.register(Account, AccountAdmin)
