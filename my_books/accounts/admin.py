from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.models import User

from .models import *
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    list_per_page = 3
    summernote_fields = ('bio',)
    list_display = ('user', 'created', 'profile_photo')
    list_filter = ['user']
    search_fields = ['user']
    prepopulated_fields = {'slug': ('user',)}
    date_hierarchy = 'created'
    ordering = ['-created']

    def profile_photo(self, object):
        if object.avatar:
            return mark_safe(f"<img src='{object.avatar.url}' width=80>")
