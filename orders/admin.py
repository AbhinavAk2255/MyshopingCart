from django.contrib import admin
from .models import OrderedItem,Order


class orederAdmin(admin.ModelAdmin):
    list_filter = ['owner','order_status']
    search_fields = ['owner','id']

# admin.site.register(OrderedItem)
admin.site.register(Order,orederAdmin)