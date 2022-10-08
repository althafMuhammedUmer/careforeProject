from django.contrib import admin
from .models import *


# Register your models here.
# class CartAdmit(admin.ModelAdmin):
    


admin.site.register(Cart)
admin.site.register(CartItem)


