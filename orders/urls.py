

from . import views
from django.urls import path


urlpatterns = [

    path('place_order', views.place_order, name='place_order'),
    path('payment_page', views.payment_page, name='payment_page'),
    
    
    path('proceed-to-pay', views.razorpaycheck),
    path('paypal', views.paypal, name="paypal"),
    path('order_complete/', views.order_complete, name='order_complete'),
    path('cash_on_delivery', views.cash_on_delivery, name="cash_on_delivery"),
    path('successpage', views.successpage, name="successpage"),
    
   
    
 
] 
