from django.contrib import admin
from .models import UrlShortener
# Register your models here.

class UrlShortenerAdmin(admin.ModelAdmin):
    list_display = ['id', 'url', 'short_url', 'times_followed']


admin.site.register(UrlShortener, UrlShortenerAdmin)
