from django.contrib import admin
from .models import *


# Register your models here.
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'Cart', 'sub_total']


admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)

