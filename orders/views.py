
from django.contrib import messages

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from Grocery.models import CartItem
from  Accounts.models import Account
from .models import Order, OrderItem, Profile
from store.models import Product
from django.contrib.auth.decorators import login_required


from .forms import OrderForm
import datetime 
import random

import json



# Create your views here.
@login_required(login_url = 'login')
def place_order(request):
    if request.method == "POST":
        print("post is working")
        
        currentuser = Account.objects.filter(id=request.user.id).first()
        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('first_name')
            currentuser.last_name = request.POST.get('last_name')
            currentuser.save()
            
        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.phone = request.POST.get('phone')
            userprofile.address = request.POST.get('address_line_1')
            userprofile.city = request.POST.get('city')
            userprofile.country = request.POST.get('country')
            userprofile.post_code = request.POST.get('post_code')
            
            userprofile.save()
                
         
        neworder = Order()
        neworder.user = request.user
        neworder.first_name = request.POST.get('first_name')
        neworder.last_name = request.POST.get('last_name')
        neworder.country = request.POST.get('country')
        neworder.address_line_1 = request.POST.get('address_line_1')
        neworder.address_line_2 = request.POST.get('address_line_2')
        neworder.city = request.POST.get('city')
        neworder.state = request.POST.get('state')
        neworder.post_code = request.POST.get('post_code')
        neworder.phone = request.POST.get('phone')
        neworder.email = request.POST.get('email')
        neworder.order_note = request.POST.get('order_note')
        
        
        cart = CartItem.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.price * item.quantity
        
        neworder.total_price = cart_total_price
        #tracking no. generator
        trackno = 'carefore' + str(random.randint(11111111,99999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno = 'carefore' + str(random.randint(11111111,99999999))
        
        #order id generator
        order_no = 'order' + str(random.randint(11111111,99999999))
        while Order.objects.filter(order_number=order_no) is None:
            order_no = 'order' + str(random.randint(11111111,99999999))
        
        neworder.tracking_no = trackno
        neworder.order_number = order_no
        neworder.save()
        # neworderitems = CartItem.objects.filter(user=request.user)
        # for item in neworderitems:
        #     OrderItem.objects.create(
        #         order = neworder,
        #         product = item.product,
        #         price = item.product.price,
        #         quantity = item.quantity,
                 
        #     )
        
            # To decrease the product quantity from available stock 
        #     orderproduct = Product.objects.filter(id=item.product_id).first()
        #     orderproduct.stock = orderproduct.stock - item.quantity
        #     orderproduct.save()
            
        # # to clear user cart 
        # CartItem.objects.filter(user=request.user).delete()
        # messages.success(request, "Your order has been placed successfully")
        
        return redirect('payment_page')
    
@login_required(login_url = 'login')
def razorpaycheck(request):
    cart = CartItem.objects.filter(user=request.user)
    total_price = 0
    for item in cart:
        total_price = total_price + item.product.price * item.quantity
        
    print(total_price)
        
        
    return JsonResponse({
        'total_price':total_price
    })
    
    
@login_required(login_url = 'login')   
def payment_page(request):
    cartitems = CartItem.objects.filter(user=request.user)
    total_price=0
    for item in cartitems:
        total_price += item.product.price * item.quantity
    tax=0
    tax = total_price*2/100
    delivery_charge = 2
    grand_total = 0
    grand_total += total_price + tax + delivery_charge
        
    order_deltails = Order.objects.filter(user=request.user).first()
    context = {
        'order':order_deltails,
        'total_price':total_price,
        'tax':tax,
        'delivery_charge':delivery_charge,
        'grand_total':grand_total,
    }
    return render(request, 'orders/payments.html', context)
    





@login_required(login_url = 'login')
def payments(request):
    body = json.loads(request.body)
    print(body)
    return render(request, 'orders/payments.html')


@login_required(login_url = 'login')
def cash_on_delivery(request):
    neworder=Order.objects.filter(user=request.user, is_ordered=False ).last()
    method = "cash on delivery"
    neworder.payment_method = method
    neworder.is_ordered = True
    
    neworder.save()
    
    
    neworderitems = CartItem.objects.filter(user=request.user)
    for item in neworderitems:
        OrderItem.objects.create(
            order = neworder,
            product = item.product,
            price = item.product.price,
            quantity = item.quantity,
                
        )
        
            # To decrease the product quantity from available stock 
        orderproduct = Product.objects.filter(id=item.product_id).first()
        orderproduct.stock = orderproduct.stock - item.quantity
        orderproduct.save()
    
                
        # to clear user cart 
    CartItem.objects.filter(user=request.user).delete()
    messages.success(request, "Your order has been placed successfully")
    return redirect('successpage')


@login_required(login_url='login')
def successpage(request):
    order_deltails = Order.objects.filter(user=request.user).last()
    
    context = {
        'order':order_deltails,
    }
    return render(request, 'orders/successpage.html', context)
    




# def place_order(request, total=0, quantity=0,):
#     current_user = request.user
#     # cart = Cart.objects.get(cart_id=_cart_id(request))
    
#     grand_total = 0
#     tax = 0
#     delivery_charge = 50
    
#     # cart = Cart.objects.get(cart_id = _cart_id(request))   
#     cart_items = CartItem.objects.filter(user=request.user, is_active=True)
#     print(cart_items)
#     for cart_item in cart_items:
#         print("inside for loop")
#         total += (cart_item.product.price * cart_item.quantity)
#         quantity += cart_item.quantity
#         print("hello")
        
#     print("total is :",total)
#     tax = (3 * total) / 100
    
#     # total_after_tax = total + tax
    
#     grand_total = total + delivery_charge + tax
    
    
    
#     if request.method == "POST":
#         print("Post is working")
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             #store billing details information inside order table
#             data = Order()
#             data.first_name     = form.cleaned_data['first_name']
#             data.last_name      = form.cleaned_data['last_name']
#             data.phone          = form.cleaned_data['phone']
#             data.email          = form.cleaned_data['email']
#             data.address_line_1 = form.cleaned_data['address_line_1']
#             data.address_line_2 = form.cleaned_data['address_line_2']
#             data.country        = form.cleaned_data['country']
#             data.state          = form.cleaned_data['state']
#             data.city           = form.cleaned_data['city']
#             data.order_note     = form.cleaned_data['order_note']
#             data.order_total    = grand_total
#             data.tax            = tax
#             data.ip            = request.META.get('REMOTE_ADDR')
#             # data.product_total = total_after_tax
#             data.save()
            
            
#              #genarate order number and store in order table
#             yr = int(datetime.date.today().strftime('%Y'))
#             dt = int(datetime.date.today().strftime('%d'))
#             mt = int(datetime.date.today().strftime('%m'))
#             d  = datetime.date(yr, mt, dt)
#             current_date = d.strftime("%d%m%Y") # like 20220305
             
#             order_number = current_date + str(data.id)
#             name = data.first_name
#             address = data.address_line_1
            
#             data.order_number = order_number
#             data.save()
#             order = Order.objects.get(order_number=order_number)
            
#             context = {
#                 'order':order,
#                 'cart_items':cart_items,
#                 'total':total,
#                 'tax': tax,
#                 'grand_total':grand_total,
#                 'name':name,
#                 'address':address,
#             }
           
#             return render(request, 'orders/payments.html', context)
        
#         else:
#             # return redirect('checkout')
#             return HttpResponse("form is invalid")
    
#     #if the cart item is less than or equal to  0 then redirect to shop or home

#     cart_count = cart_items.count()
#     if cart_count <= 0:
        
#         return HttpResponse("your cart is empty")
   
    
            
            
