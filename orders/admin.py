from django.contrib import admin
from .models import *

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    model=Order
    list_display = ['id','order_number','full_name', 'address_line_1', 'state', 'country','post_code', 'phone', 'total_price', 'status']


admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Profile)
admin.site.register(Payment)


    




