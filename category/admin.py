from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name', 'slug')
admin.site.register(Category,CategoryAdmin) 

class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('subcategory_name',)}
    list_display=('subcategory_name','slug','enter_date','category')    

admin.site.register(SubCategory,SubCategoryAdmin)

# class ItemAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('item_name',)}
#     list_display = ('item_name', 'slug', 'category', 'item_img')
    
# admin.site.register(Items, ItemAdmin)


