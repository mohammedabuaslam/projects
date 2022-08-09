from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Orders


class AccountAdmin(UserAdmin):
	list_display = ('email', 'username', 'phone', 'credits','is_staff', 'email_verified','date_joined', 'last_login',)
	search_fields = ('email', 'username', 'phone',)
	readonly_fields = ('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()



@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
	list_display = Orders.displayfields
	list_filter = Orders.filterfields

admin.site.register(User, AccountAdmin)
