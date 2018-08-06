from django.contrib import admin
from .models import MainURL


class URLModelAdmin(admin.ModelAdmin):
    list_display = ['url', 'shortcode', 'timestamp']
    list_display_links = ['shortcode']
    list_editable = ['url']
    list_filter = ['shortcode', 'timestamp']
    search_fields = ['url', 'shortcode']

    class Meta:
        model = MainURL


admin.site.register(MainURL, URLModelAdmin)
