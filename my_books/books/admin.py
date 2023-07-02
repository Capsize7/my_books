from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ['title', 'author', 'photo', 'description', 'status', 'rating', 'published']
    list_filter = ['status', 'author', 'genre']
    search_fields = ['title', 'author']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published'
    ordering = ['-published']


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
