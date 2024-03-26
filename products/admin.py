from django.contrib import admin
from . models import product,newproducts

# Register your models here.
@admin.register(newproducts)
class Admin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'category',
        'image',
        'new_price',
        'old_price'
    ]

    


admin.site.register(product)