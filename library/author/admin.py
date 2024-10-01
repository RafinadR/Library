from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname", "patronymic")
    search_fields = ('name', 'surname', 'patronymic')
    list_display_links = ('id', 'name')
    
    
    fieldsets = (
        (None, {'fields': ('name', 'surname', 'patronymic')}),
        ('Books', {'fields': ('books',)}),
    )
    
    ordering = ('id',)
    filter_horizontal = ["books"]


admin.site.register(Author, AuthorAdmin)