from .models import CartItem



def counter(request):
    cart_count = 0
    try:
        cart = CartItem.objects.filter(user=request.user.id)
        
        for cart_item in cart:
            cart_count += cart_item.quantity
            
        
    except CartItem.DoesNotExist:
        cart_count = 0
   
    return dict(cart_count=cart_count)


            