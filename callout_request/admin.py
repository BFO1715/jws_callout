from django.contrib import admin
from .models import Request
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Request)
class RequestAdmin(SummernoteModelAdmin):

    list_display = ('description', 'slug', 'created_on')
    search_fields = ['description', 'content']
    list_filter = ('created_on')
    prepopulated_fields = {'slug': ('description',)}
    summernote_fields = ('content',)

