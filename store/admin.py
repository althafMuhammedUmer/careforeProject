from django.contrib import admin
from .models import Product, ProductGallery, WishList, HomeBanner
import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1
    

@admin_thumbnails.thumbnail('images')
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock',  'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    search_fields = ('product_name',)
    inlines = [ProductGalleryInline]
    



    
 
    
    

  

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductGallery)
admin.site.register(WishList)
admin.site.register(HomeBanner)

