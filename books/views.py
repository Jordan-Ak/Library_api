from rest_framework import viewsets, mixins
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter
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

    filter_fields = ('username', 'email', 'date_joined',)
    search_fields = ('^username', '^email')
    ordering_fields = ('username', 'email', 'date_joined')

    def get_queryset(self): #Query set filters according to being a staff, staff gets all users.
                            #User gets only himself

        if self.request.user.is_staff:
            queryset = get_user_model().objects.all()
        
        else:
            queryset = get_user_model().objects.filter(id = self.request.user.id)
        
        return queryset

 
class AuthorViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorDetailSerializer
    serializer_action_classes = {'list': serializers.AuthorListSerializer,}
    permission_classes = [IsAdminOrReadOnly,permissions.IsAuthenticated,]

    filter_fields = ('name',)
    search_fields = ('^name')
    ordering_fields = ('name',)
    
class PublisherViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):

    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherDetailSerializer
    serializer_action_classes = {'list': serializers.PublisherListSerializer,}
    permission_classes = [IsAdminOrReadOnly, permissions.IsAuthenticated,]

    filter_fields = ('name',)
    search_fields = ('^name')
    ordering_fields = ('name',)

class GenreViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):

    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreDetailSerializer
    serializer_action_classes = {'list': serializers.GenreListSerializer,}
    permission_classes = [IsAdminOrReadOnly, permissions.IsAuthenticated,]

    filter_fields = ('name',)
    search_fields = ('^name')
    ordering_fields = ('name',)

class BookViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):

    queryset = models.Book.objects.all()
    serializer_class = serializers.BookDetailSerializer
    serializer_action_classes = {'list': serializers.BookListSerializer}
    permission_classes = [IsAdminOrReadOnly, permissions.IsAuthenticated,]

    filter_fields =  ('name','authors','rating','genre')
    search_fields = ('name','authors','rating', 'genre')
    ordering_fields = ('name','authors','rating', 'genre')

class BorrowedViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BorrowedSerializer
    permission_classes = [IsAdminOrReadOnly, permissions.IsAuthenticated,]
    filter_fields = ('who_borrowed','name','has_returned','borrowed_date','returned_date',)
    search_fields = ('who_borrowed','name','borrowed_date','returned_date',)
    ordering_fields = ('who_borrowed','name','has_returned','borrowed_date','returned_date',)

    def get_queryset(self): #Query set filters according to being a staff, staff gets all users.
                            #User gets only himself

        if self.request.user.is_staff:
            queryset = models.Borrowed.objects.all()
        
        else:
            queryset = models.Borrowed.objects.filter(who_borrowed = self.request.user.id)
        
        return queryset    

class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RatingSerializer
    
    def get_queryset(self):  #Filter ratings so user sees only his own rating.
        if self.request.user.is_staff:
            queryset = models.Rating.objects.all()
        
        else:
            queryset = models.Rating.objects.filter(who_rated = self.request.user.id)
        
        return queryset 

class QuantityTimeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuantityBorrowedSerializer

    def get_queryset(self):  #Filter ratings so user sees only his own rating.
        if self.request.user.is_staff:
            queryset = models.Quantity_Borrowed.objects.all()
        
        else:
            queryset = models.Quantity_Borrowed.objects.filter(who= self.request.user.id)
        
        return queryset
    
    
        
    