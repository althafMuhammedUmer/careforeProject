from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock',  'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    search_fields = ('product_name',)
  

# Register your models here.
admin.site.register(Product,ProductAdmin)

