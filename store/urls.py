

from . import views
from django.urls import path


urlpatterns = [
   
 
    path('store/', views.store, name='store'),
    # path('<slug:category_slug>/', views.shop, name='products_by_categroy'),
  
   

    
] 
