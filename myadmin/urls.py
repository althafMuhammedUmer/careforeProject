from django.urls import path
from .import views


urlpatterns = [
    # path('myadminpage',views.myadmin, name="myadmin"),
    path('myadminlogout/', views.myadminlogout, name='myadminlogout'),
    path('userdata/', views.userdata, name='userdata'),
    path('user_delete/<int:id>/', views.user_delete, name="user_delete"),
    path('user_block/<int:id>/', views.user_block, name="user_block"),
    # path('product_details/', views.product_details, name='product_details'),
    path('product_delete/<int:id>/', views.product_delete, name='product_delete'),
   
    path('myadmin2/', views.myadmin2, name="myadmin2"),
    path('product_details/', views.product_details, name="product_details"),
    path('add_product', views.add_product, name="add_product"),
    path('update_product/<int:pk>/', views.update_product, name="update_product"),
    path('delete_product/<int:pk>/', views.delete_product, name="delete_product"),
    
    
    
    path('category_list/',views.CategoryListView.as_view(), name= "category_list"),
    path('category_update/<slug:pk>',views.CategoryUpdate.as_view(), name="category_update"),
    path('category_delete/<int:pk>/', views.category_delete, name="category_delete"),
    
    path('category_create/',views.CategoryCreate.as_view(), name= "category_create"),
    
    path('view_orders', views.view_orders, name="view_orders"),
    path('viewSingleOrder/<int:id>/', views.viewSingleOrder, name="viewSingleOrder"),
    path('ordercompleted/<int:id>/', views.ordercompleted, name="ordercompleted"),
    path('orderpending/<int:id>/', views.orderpending, name="orderpending"),
    path('ordershipping/<int:id>/', views.ordershipping, name="ordershipping"),
    path('ordercancel/<int:id>/', views.ordercancel, name="ordercancel"),
    
    
    
    
    
]
