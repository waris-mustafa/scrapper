from django.contrib import admin

from .models import Scrape


@admin.register(Scrape)
class ScrapeAdmin(admin.ModelAdmin):
    list_display = ['user', 'url', 'created_at']
    search_fields = ['user__email', 'url']
