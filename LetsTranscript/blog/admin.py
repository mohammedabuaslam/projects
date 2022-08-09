from django.contrib import admin
from .models import blog

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'url', 'date_posted', )
	search_fields = ('title', 'url',)
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(blog, BlogAdmin)