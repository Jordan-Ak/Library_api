from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

#Configuration to allow proper viewing in admin site
CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):    
    add_form = CustomUserCreationForm    
    form = CustomUserChangeForm    
    model = CustomUser    
    list_display = ['id','email', 'username','is_staff',]

admin.site.register(CustomUser, CustomUserAdmin)
