from django.contrib import admin
from .models import Request, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Request)
class RequestAdmin(SummernoteModelAdmin):

    list_display = ('description', 'slug', 'created_on')
    search_fields = ['description', 'content']
    list_filter = ('description', 'created_on')
    prepopulated_fields = {'slug': ('description',)}
    summernote_fields = ('content',)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'request', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
