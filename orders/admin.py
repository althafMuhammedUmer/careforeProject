from django.contrib import admin
from .models import *

# Register your models here.
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price', 'ordered',)
    


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email' ,'city', 'state', 'order_total', 'tax', 'status', 'is_ordered' ,'created_at']
    list_filter =['status', 'is_ordered']   
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email ']
    list_per_page = 20
    inlines = [OrderProductInline]
    
    
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'payment_id', 'payment_method', 'amount_paid', 'status']  

admin.site.register(Order, OrderAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(OrderProduct)





