from rest_framework import viewsets, mixins
from django.contrib.auth import get_user_model
from rest_framework import permissions
from . import models
from . import serializers
from .permissions import IsAdminOrReadOnly
from .mixins import GetSerializerClassMixin


# Create your views here.

class UserViewSet(#mixins.CreateModelMixin,   #No post method but the rest are avaialble
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):  
    
    #Project-level permissions apply here, authenticated only
    serializer_class = serializers.UserSerializer
    lookup_field = 'username'

    def get_queryset(self): #Query set filters according to being a staff, staff gets all users.
                            #User gets only himself

        if self.request.user.is_staff:
            queryset = get_user_model().objects.all()
        
        else:
            queryset = get_user_model().objects.filter(id = self.request.user.id)
        
        return queryset

 
class AuthorViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorListSerializer
    serializer_action_classes = {'detail': serializers.AuthorDetailSerializer,}
    permission_classes = [IsAdminOrReadOnly,]
    