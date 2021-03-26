from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#Forms added for easy manipulation in admin
class CustomUserCreationForm(UserCreationForm):
    class Meta:        
        model = get_user_model()        
        fields = ('first_name', 'last_name','username','email', 'phone_no')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name','username','email', 'phone_no')