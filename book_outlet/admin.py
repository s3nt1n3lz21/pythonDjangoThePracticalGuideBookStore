from django.contrib import admin

from .models import Author, Book, Address

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("rating", "author",)
    list_display = ("title", "author")

class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("last_name",)
    list_display = ("first_name", "last_name")

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address)
