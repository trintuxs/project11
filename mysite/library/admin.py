from django.contrib import admin

from .models import Author, Genre, Book, BookInstance


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    list_filter = ('status', 'due_back')
    search_fields = ('id', 'book__title')
    search_fields = ['foreign_key__related_fieldname']

    fieldsets = (
        ('General', {'fields': ('uuid', 'book')}),
        ('Availability', {'fields': ('status', 'due_back')}),
    )
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'display_books')




admin.site.register(Book)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(BookInstance)