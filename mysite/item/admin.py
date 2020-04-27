from webbrowser import register
from django.contrib import admin

# Register your models here.
from item.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'item_name', 'item_amount', 'item_image', 'create_date', 'update_date']
    page = 20
    search_fields = ['item_name']

admin.site.register(Item, ItemAdmin)
