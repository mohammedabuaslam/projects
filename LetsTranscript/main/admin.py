from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Sitemaps

class SitemapAdmin(admin.ModelAdmin):
	list_display = ('sitemapurl',)
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
admin.site.register(Sitemaps, SitemapAdmin)