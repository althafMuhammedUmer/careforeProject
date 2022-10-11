from django.urls import path
from .import views

urlpatterns = [
    path('register/',views.register, name='register' ),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('my_orders', views.my_orders, name="my_orders"),
    # path('', views.dashboard, name='dashboard'),
    path('verify', views.verify_code, name='verify_code')
    
    
    
    
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
]

