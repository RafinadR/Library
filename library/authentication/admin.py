from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    
    readonly_fields = ['created_at']
    
    list_display = ('id', 'first_name', 'last_name','email',  'role', 'is_active', 'is_staff', 'is_superuser', 'created_at')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'role')
    
    list_display_links = ('id', 'first_name')

    date_hierarchy = "created_at"
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'middle_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'role')}),
        ('Some dates', {'fields': ('created_at',)})
        
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'middle_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'role')}
         ),
    )

    ordering = ('id',)
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)
