from django.contrib import admin
from ecan.models import Ecan, Item 


class ItemInline(admin.StackedInline):
	model = Item
	extra = 0

class EcanAdmin(admin.ModelAdmin):
	fieldsets = [
		('Location',{'fields': ['address' ,'latitude', 'longitude', 'ip']}),
	]
	inlines = [ItemInline]
	list_filter = ['created']
	search_fields = ['address']

admin.site.register(Ecan, EcanAdmin)

admin.site.register(Item)
