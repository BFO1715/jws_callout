from django.contrib import admin
from .models import Request
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Request)
class RequestAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)