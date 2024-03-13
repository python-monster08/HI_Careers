# authentication/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'mobile_number', 'is_admin', 'is_teacher', 'is_student', 'is_active']
    list_filter = ['is_admin', 'is_teacher', 'is_student', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'mobile_number', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_teacher', 'is_student', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'mobile_number', 'password1', 'password2'),
        }),
        ('Permissions', {'fields': ('is_admin', 'is_teacher', 'is_student', 'is_active')}),
    )
    search_fields = ['email', 'mobile_number']
    ordering = ['-created_at']

    # Exclude non-editable fields
    exclude = ['created_at']

admin.site.register(CustomUser, CustomUserAdmin)
 