from django.urls import path
from .import views

urlpatterns = [
    path('register/',views.register, name='register' ),
    path('loginpage/', views.loginpage, name='login'),
    path('logoutpage/', views.logoutpage, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('', views.dashboard, name='dashboard'),
    path('verify', views.verify_code, name='verify_code'),
   
    
    
    
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
]

