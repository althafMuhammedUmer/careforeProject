

from . import views
from django.urls import path


urlpatterns = [
   
 
    path('', views.store, name='store'),
    
    
    path('<slug:category_slug>', views.store, name="products_by_categroy"),
    path('search/',views.search, name='search'),
    path('product_details/<slug>/', views.product_details, name='product_details'),
    path('addwishlist', views.addwishlist, name="addwishlist"),
    path('wishlist/', views.viewWishlist, name="wishlist"),
    path('deletewishlist/<int:product_id>/', views.deletewishlist, name="deletewishlist"),
    
    
    # path('deletewishlist/<int:product_id>/', views.deletewishlist, name="deletewishlist"),
    
    # path('<slug:category_slug>/', views.shop, name='products_by_categroy'),
  
   

    
] 
