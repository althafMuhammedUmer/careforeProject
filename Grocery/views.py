
from category.models import Category,SubCategory
from django.shortcuts import render,redirect,get_object_or_404
from store.models import Product
from .models import  CartItem
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required



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
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
       
        product = Product.objects.filter(Q(product_name__icontains=keyword) | Q(description__icontains = keyword))
         
        context = {
            'products':product
        } 
    
    return render(request,'Home_page/index.html', context)  





def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    
    
    # guest user
    
    



        
def cart_view(request, total=0, quantity=0, cart_items = None):
    products_list = Product.objects.all().filter(is_available=True)
    category_list = Category.objects.all()
    
    
    
    return render(request, 'Home_page/shopping-cart.html' )      





def remove_cart(request,product_id):
    # cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, user=request.user)
    
    if cart_item.quantity > 1 :
        cart_item.quantity -= 1
        cart_item.save()
        
    else:
        cart_item.delete()
    return redirect('cart_view')
    
def remove_cart_item(request,product_id):
    # cart = Cart.objects.get(cart_id = _cart_id(request))  
    # product = get_object_or_404(Product, id=product_id)
    # cart_item = CartItem.objects.get(product=product, Cart=cart)
    # cart_item.delete()
    return redirect('cart_view')
    
    
@login_required(login_url='login')    
def checkout(request, total=0, quantity=0, cart_items = None):
    products_list = Product.objects.all().filter(is_available=True)
    category_list = Category.objects.all()
    tax=0
    grand_total=0
    checkout_total=0
    delivery_charge=0
    
   
    try:
        # cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = ( 3 * total )/100
        # grand_total = tax + total
        
        
        delivery_charge = 50
        checkout_total = delivery_charge + total
        grand_total = total + tax + delivery_charge
    except ObjectDoesNotExist:
        pass
    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'grand_total':grand_total,
        'products':products_list,
        'category': category_list,
        'checkout_total':checkout_total,
        'delivery_charge':delivery_charge
        
    }
    
    return render(request, 'Home_page/checkout.html', context)
    