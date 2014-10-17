from django.contrib import admin
from ecan.models import Ecan, Item 


class ItemInline(admin.StackedInline):
	model = Item
	extra = 1

class ManageAdmin(admin.ModelAdmin):
	fieldsets = [
		('Location',{'fields': ['address' ,'latitude', 'longitude']}),
	]
	inlines = [ItemInline]
	list_filter = ['created']
	search_fields = ['address']

admin.site.register(Ecan, ManageAdmin)

