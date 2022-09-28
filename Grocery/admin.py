from django.contrib import admin
from .models import *


# Register your models here.
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'sub_total']


admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)

