

from category.models import Category,SubCategory
from django.shortcuts import render,redirect,get_object_or_404
from store.models import Product

from .models import  CartItem
from orders.models import Order, Profile
from django.http import HttpResponse, JsonResponse

from django.contrib.auth.decorators import login_required
from django.contrib import messages



from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
# def _cart_id(request):
#     cart = request.session.session_key
#     if not cart:
#         cart = request.session.create()
#     return cart



# def index(request):
#     category_list = Category.objects.all()
#     print (category_list)
#     products_list = Product.objects.all().filter(is_available=True)
#     subcategory_list = SubCategory.objects.all()
    
#     context = {
#         'products':products_list,
#         'category':category_list,
#         'subcategory':subcategory_list
#     }
    
#     return render(request,'Home_page/index.html', context)
####################################################################
 




@login_required(login_url='login')
def addtocart(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = request.POST.get('product_id')
            print(prod_id)
            
            product_check = Product.objects.get(id=prod_id)
            print(product_check)
            if product_check:
                if (CartItem.objects.filter(user=request.user.id, product_id=prod_id)):
                    
                    return JsonResponse({'status': "product already in the cart"})
                
                else:
                    prod_qty = int(request.POST.get('product_qty'))
                    
                    if product_check.stock >= prod_qty:
                        CartItem.objects.create(user=request.user, product_id=prod_id, quantity=prod_qty)
                        return JsonResponse({'status': "product added successfully"})
                    else:
                        return JsonResponse({'status': "Only " + str(product_check.stock)+ " quantity available"})
            else:
                return JsonResponse({'status': "No such products found"})
            
        else:
            
            
            
            return JsonResponse({'status':"login to continue"})
        
     
    return redirect('/')
    
    
    
        
    # product = Product.objects.get(id=product_id)
    
    
    
    # guest user
    
    



@login_required(login_url='login' )       
def cart_view(request):
    if request.user.is_authenticated:
        categories = Category.objects.all()
        
    
        
        carts = CartItem.objects.filter(user=request.user).order_by('-created_at')
        
        
        total_price=0
        for item in carts:
            total_price = total_price + item.product.price * item.quantity
        tax = 0
        tax += total_price * 2/100
        delivery_charge = 2
        grand_total=0
        grand_total = total_price + tax + delivery_charge    
        
        context = {
            'categories':categories,
            'carts':carts,
            'total_price':total_price,
            'tax':tax,
            'delivery_charge':delivery_charge,
            'grand_total':grand_total,
            
            
        }
    
        return render(request, 'Home_page/shopping-cart.html', context )
    
    else:
        return redirect('login')
    
@login_required(login_url = 'login')    
def updatecart(request):
    if request.method == "POST":
        prod_id = request.POST.get('product_id')
        if CartItem.objects.filter(user=request.user, product_id=prod_id):
            prod_qty = int(request.POST.get('product_qty'))
            cartitem = CartItem.objects.get(product_id = prod_id, user=request.user)
            cartitem.quantity = prod_qty
            cartitem.save()
            
            return JsonResponse({'status': "updated successfully"})
    return redirect('/')

# def deletecartitem(request):
#     if request.method == "POST":
#         prod_id = request.POST.get('product_id')
#         if CartItem.objects.filter(user=request.user, product_id=prod_id):
#             cartitem = CartItem.objects.get(user=request.user, product_id=prod_id)
#             cartitem.delete()
#             return JsonResponse({'status': "deleted successfully"})
#     return redirect('/')
            
            
            
        




@login_required(login_url = 'login')
def remove_cart(request,product_id):
    # cart = Cart.objects.get(cart_id = _cart_id(request))
    product_id = Product.objects.get(id=product_id)
    cart_item = CartItem.objects.get(product_id=product_id, user=request.user)
    
    # if cart_item.quantity > 1 :
    #     cart_item.quantity -= 1
    #     cart_item.save()
        
    # else:
    cart_item.delete()
    messages.success(request,'deleted successfully')
    return redirect('cart_view')



@login_required(login_url = 'login')
def checkout(request):
    rawcart = CartItem.objects.filter(user=request.user)
    for item in rawcart:
        if item.quantity > item.product.stock:
            CartItem.objects.delete(id=item.id)
    
    cartitems = CartItem.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.price * item.quantity
    tax = 0
    tax = total_price*2/100
    print(tax)
    delivery_charge = 2
    grand_total = 0
    grand_total += total_price + tax + delivery_charge
    print(grand_total)
    
    userprofile = Profile.objects.filter(user=request.user).first()
    
    
    
    context = {
        'cartitems':cartitems,
        'total_price':total_price,
        'tax':tax,
        'delivery_charge':delivery_charge,
        'grand_total':grand_total,
        'userprofile':userprofile,
        
    }
    return render(request, 'Home_page/checkout.html', context)
     
    

    
    
# @login_required(login_url='login')    
# def checkout(request, total=0, quantity=0, cart_items = None):
#     products_list = Product.objects.all().filter(is_available=True)
#     category_list = Category.objects.all()
#     tax=0
#     grand_total=0
#     checkout_total=0
#     delivery_charge=0
    
   
#     try:
#         # cart = Cart.objects.get(cart_id = _cart_id(request))
#         cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        
#         for cart_item in cart_items:
#             total += (cart_item.product.price * cart_item.quantity)
#             quantity += cart_item.quantity
#         tax = ( 3 * total )/100
#         # grand_total = tax + total
        
        
#         delivery_charge = 50
#         checkout_total = delivery_charge + total
#         grand_total = total + tax + delivery_charge
#     except ObjectDoesNotExist:
#         pass
#     context = {
#         'total':total,
#         'quantity':quantity,
#         'cart_items':cart_items,
#         'tax':tax,
#         'grand_total':grand_total,
#         'products':products_list,
#         'category': category_list,
#         'checkout_total':checkout_total,
#         'delivery_charge':delivery_charge
        
#     }
    
#     return render(request, 'Home_page/checkout.html', context)


# def wishlist(request):
#     pass
    # return render(request, 'Home_page/wishlist.html')
    