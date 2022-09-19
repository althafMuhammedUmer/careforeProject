from django.shortcuts import render, redirect
from django.http import HttpResponse
from Grocery.models import CartItem
from .models import Order
from .forms import OrderForm
import datetime 

# Create your views here.
def place_order(request, total=0, quantity=0,):
    current_user = request.user
    grand_total = 0
    tax = 0
    cart_items = CartItem.objects.filter(user=current_user)
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_items.quantity)
        quantity += cart_item.quantity

    tax = (2 * total) / 100
    grand_total = total + tax 
    
    
    if request.method == "POST":
        print("Post is working")
        form = OrderForm(request.POST)
        if form.is_valid():
            #store billing details information inside order table
            data = Order()
            data.first_name     = form.cleaned_data['first_name']
            data.last_name      = form.cleaned_data['last_name']
            data.phone          = form.cleaned_data['phone']
            data.email          = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country        = form.cleaned_data['country']
            data.state          = form.cleaned_data['state']
            data.city           = form.cleaned_data['city']
            data.order_note     = form.cleaned_data['order_note']
            data.order_total    = grand_total
            data.tax            = tax
            data.ip            = request.META.get('REMOTE_ADDR')
            data.save()
            
             #genarate order number and store in order table
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d  = datetime.date(yr, mt, dt)
            current_date = d.strftime("%d%m%Y") # like 20220305
             
            order_number = current_date + str(data.id)
            
            data.order_number = order_number
            data.save()
            print(data)
            print("its working")
            return redirect('checkout')
        
        else:
            # return redirect('checkout')
            return HttpResponse("form is invalid")
    
    #if the cart item is less than or equal to  0 then redirect to shop or home

    cart_count = cart_items.count()
    if cart_count <= 0:
        
        return HttpResponse("your cart is empty")
    
    
            
            
