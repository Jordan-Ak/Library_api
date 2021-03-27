from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
#Configuration to allow proper viewing in admin site


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
      
    list_display = ['id','email', 'username','is_staff',]


admin.site.register(CustomUser, CustomUserAdmin)
