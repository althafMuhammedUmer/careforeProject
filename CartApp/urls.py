from . import views
from django.urls import path


urlpatterns = [

    # path('place_order', views.place_order, name='place_order'),
    path('add-to-cart/', views.add_cart, name='add_cart'),
    
    
 
] 