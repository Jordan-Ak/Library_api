from rest_framework import viewsets
from django.contrib.auth import get_user_model
from . import models
from . import serializers

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    #queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
    

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = get_user_model().objects.all()
        
        else:
            queryset = get_user_model().objects.filter(id = self.request.user.id)
        
        return queryset
    