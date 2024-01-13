from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
     list_display = ('id','product_name','product_info','product_price')
     list_display_links = ('product_name',)
     list_editable = ('product_info',)
     search_fields = ('product_price', 'product_name' )
     ordering = ['id']
     save_on_top = True


admin.site.register(Catalog)