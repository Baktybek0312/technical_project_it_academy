from django.contrib import admin

from .models import InfoHabrs


@admin.register(InfoHabrs)
class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title'
    )
    list_display_links = (
        'title',
    )
    search_fields = (
        'id', 'title'
    )
