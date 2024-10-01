from django.contrib import admin
from .models import Book


class AuthorInline(admin.TabularInline):
    model = Book.authors.through

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("name", "description")
    list_filter = ("name", "authors" )
    list_display = ("id", "name","get_book_author", "count")
    search_fields = ('name',)
    list_display_links = ('id', 'name')
    inlines = [AuthorInline]
    
    fieldsets = (
        (None, {'fields': ('name',)}),
        ('Description', {'fields': ('description',)}),
        ('Count', {'fields': ('count',)})
        
        
    )
    
    ordering = ('id',)
    filter_horizontal = ["authors"]
    
    
    def get_book_author(self, obj):
        return ", ".join([f"{author.name} {author.surname}"for author in obj.authors.all()])

    get_book_author.short_description = 'Authors'