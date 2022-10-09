from  django.urls import path
from . import views


urlpatterns = [
    # path('',views.index, name='index'),
    path('search/',views.search, name='search'),
    # path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('add-to-cart', views.addtocart, name="addtocart"),
    path('update-cart', views.updatecart, name="updatecart"),
    # path('delete-cart-item', views.deletecartitem, name="deletecartitem"),
    
    # path('wishlist', view.wishlist, name="wishlist")
    
    
    

    path('cart_view/',views.cart_view, name='cart_view' ),
    
    path('remove_cart/<int:product_id>/',views.remove_cart, name='remove_cart'),
   
    
    path('checkout/',views.checkout, name='checkout'),
    
   
    
]

