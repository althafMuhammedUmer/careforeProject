from django.contrib import admin
from .models import Banner, Product, ProductAttribute

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag','product_name', 'stock',  'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    search_fields = ('product_name',)

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'color', 'storage', )
    
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag', 'text', )

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductAttribute,ProductAttributeAdmin)
admin.site.register(Banner,BannerAdmin)


