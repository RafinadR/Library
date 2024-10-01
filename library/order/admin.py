from django.contrib import admin
from .models import Order


class NameFilter(admin.SimpleListFilter):
    title = 'Order by name'
    parameter_name = 'name'

    def lookups(self, request, model_admin):
        return [
            ('a_z', 'a - z'),
            ('z_a', 'z - a')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'a_z':
            return queryset.all().order_by('name')
        elif self.value() == 'z_a':
            return queryset.all().order_by('-name')



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = [NameFilter, "user"]
    readonly_fields = ['created_at']
    
    list_display = ("id", "book", "user", "created_at", "end_at", "plated_end_at")
    search_fields = ('user', 'book')
    list_display_links = ('id',)
    
    fieldsets = (
        (None, {'fields': ('book', 'user')}),
        ('Important dates', {'fields': ('created_at', 'end_at', 'plated_end_at')}),
    )
    date_hierarchy = "created_at"
    ordering = ('id',)
    filter_horizontal = []

