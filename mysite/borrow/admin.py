from django.contrib import admin
from .models import Borrow, Borrow_Item


class BorrowAdmin(admin.ModelAdmin):
    list_display = ['id', 'request_date', 'borrow_date', 'status', 'return_date']

class Borrow_ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'borrow_id', 'item_id', 'borrow_amount']

admin.site.register(Borrow, BorrowAdmin)
admin.site.register(Borrow_Item, Borrow_ItemAdmin)