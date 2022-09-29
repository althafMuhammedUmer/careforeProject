from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Account

# Register your models here.
class AccountAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'date_joined' ,'last_login', 'is_active')
    list_display_links = ('email', 'username',)
   
    
    
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
    
      
    
    

admin.site.register(Account,AccountAdmin)
# admin.site.register(Profile)


####

