from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):
    list_per_page = 5
    summernote_fields = ('description',)
    list_display = ['title', 'author', 'book_photo', 'status', 'rating', 'published',]
    list_filter = ['status', 'genre']
    search_fields = ['title', 'author']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published'
    ordering = ['-published']
    list_editable = ('status', 'rating')

    def book_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=70>")


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ['name', 'email', 'book', 'created', 'author']
    list_filter = ['created', 'author']
    search_fields = ['name', 'email']
    ordering = ['created']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


