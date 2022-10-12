from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Account, UserProfile
from django.utils.html import format_html

# Register your models here.
class AccountAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'date_joined' ,'last_login', 'is_active')
    list_display_links = ('email', 'username',)
   
    
    
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    
    list_display = ['thumbnail', 'username', 'full_address', 'city', 'state', 'country']
    
    
    
    
      
    
    

admin.site.register(Account,AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)


####

