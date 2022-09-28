
from email.mime import image
from turtle import color
from category.models import Category,SubCategory
from django.shortcuts import render,redirect,get_object_or_404
from store.models import Product, ProductAttribute
from .models import Cart, CartItem
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required



from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart



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
        product_count = product.count()
        print(product_count)
        

         
        context = {
       
            'product':product,
            'product_count':product_count,
        } 
    
    return render(request,'Home_page/index.html', context)  





def add_cart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id)
    
    # is_cart_item_exists = CartItem.objects.filter(product=product,user=current_user).exists()
    
    
    
    # if     user
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        print("cart try inside")
        
        
    except Cart.DoesNotExist:
        print("no cart is saved")
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        
    
    cart.user = request.user
    cart.save()
    
    try: # for quantity increment
        cart_item = CartItem.objects.get(product = product, Cart=cart)
        
        
        cart_item.quantity += 1 #cart_item.quantity = cartItem.quantity + 1
        cart_item.save()
        
        return redirect('cart_view')
        
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            Cart = cart,
            user = request.user
        )
        
        cart_item.save()
        return redirect('cart_view')
  




        
def cart_view(request, total=0, quantity=0, cart_items = None):
    products_list = Product.objects.all().filter(is_available=True)
    product_image = Product.objects.values('productattribute')
    category_list = Category.objects.all()
    # print(product_image)
    
    
    
    try:
        tax = 0
        grand_total = 0
        # if request.user.is_authenticated:
        #     cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        # else: 
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(Cart=cart, is_active=True)
        for cart_item in cart_items:
            # total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = ( 3 * total )/100
        grand_total = tax + total
    
    except ObjectDoesNotExist:
        print("object does not exist in cart")
    
    context = {
        # 'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'product_attribute':product_image,
        # 'tax':tax,
        # 'grand_total':grand_total,
        'product':products_list,
        'category': category_list,
        
    }
    
    
    return render(request, 'Home_page/shopping-cart.html' , context)      





def remove_cart(request,product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, Cart=cart)
    
    if cart_item.quantity > 1 :
        cart_item.quantity -= 1
        cart_item.save()
        
    else:
        cart_item.delete()
    return redirect('cart_view')
    
def remove_cart_item(request,product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))  
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, Cart=cart)
    cart_item.delete()
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
            # total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = ( 3 * total )/100
        # grand_total = tax + total
        
        
        delivery_charge = 50
        # checkout_total = delivery_charge + total
        # grand_total = total + tax + delivery_charge
    except ObjectDoesNotExist:
        pass
    context = {
        # 'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        # 'tax':tax,
        # 'grand_total':grand_total,
        'products':products_list,
        'category': category_list,
        # 'checkout_total':checkout_total,
        'delivery_charge':delivery_charge
        
    }
    
    
    return render(request, 'Home_page/checkout.html', context)

    