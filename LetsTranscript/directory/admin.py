from django.contrib import admin
from .models import Directory, Sidelinks

@admin.register(Directory)
class OrderAdmin(admin.ModelAdmin):
	list_display = Directory.displayfields
	list_filter = Directory.filterfields

@admin.register(Sidelinks)
class OrderAdmin(admin.ModelAdmin):
	list_display = Sidelinks.displayfields
	list_filter = Sidelinks.filterfields
