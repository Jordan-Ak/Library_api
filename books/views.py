from rest_framework import viewsets, mixins
from django.contrib.auth import get_user_model
from rest_framework import permissions
from . import models
from . import serializers


# Create your views here.

class UserViewSet(#mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    
    serializer_class = serializers.UserSerializer
    lookup_field = 'username'

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = get_user_model().objects.all()
        
        else:
            queryset = get_user_model().objects.filter(id = self.request.user.id)
        
        return queryset
    