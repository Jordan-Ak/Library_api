from rest_framework import viewsets, mixins
from rest_framework import filters
from rest_framework.response import Response
from django_filters import FilterSet
from django.contrib.auth import get_user_model
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter,CharFilter, BooleanFilter
from django_property_filter import (PropertyNumberFilter, PropertyCharFilter, 
                                    PropertyFilterSet,PropertyDurationFilter)
from . import models
from . import serializers
from .permissions import IsAdminOrReadOnly
from .mixins import GetSerializerClassMixin


# Create your views here.
class UserFilter(FilterSet):
    from_date_joined = DateTimeFilter(field_name = 'date_joined', lookup_expr = 'gte')
    to_date_joined = DateTimeFilter(field_name = 'date_joined', lookup_expr = 'lte')
    user_name = AllValuesFilter(field_name = 'username',)
    e_mail = AllValuesFilter(field_name = 'email',)
    username = CharFilter(field_name = 'username', lookup_expr = 'icontains')
    email = CharFilter(field_name = 'email', lookup_expr = 'icontains')
    
    class Meta:
        model = get_user_model()
        fields = ('username','email','from_date_joined', 'to_date_joined', 'user_name','e_mail',)

class UserViewSet(#mixins.CreateModelMixin,   #No post method but the rest are avaialble
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):  
    
    #Project-level permissions apply here, authenticated only
    serializer_class = serializers.UserSerializer
    lookup_field = 'username'

    filter_class = UserFilter  #Bugs to fix filter doesn't work well
    search_fields = ('^username', '^email')                #Search is okay
    ordering_fields = ('username', 'email', 'date_joined')  # Ordering fields is okay

    def get_queryset(self): #Query set filters according to being a staff, staff gets all users.
                            #User gets only himself

        if self.request.user.is_staff:
            queryset = get_user_model().objects.all()
        
        else:
            queryset = get_user_model().objects.filter(id = self.request.user.id)
        
        return queryset

 

class AuthorFilter(FilterSet):
    author_name = CharFilter(field_name = 'name', lookup_expr = 'icontains',)

    class Meta:
        model = models.Author
        fields = ('author_name',)


class AuthorViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorDetailSerializer
    serializer_action_classes = {'list': serializers.AuthorListSerializer,}
    permission_classes = [IsAdminOrReadOnly,permissions.IsAuthenticated,]

     #Everything's calm
    filter_class = AuthorFilter
    search_fields = ['^name']
    ordering_fields = ('name',)
    
class PublisherFilter(FilterSet):
    name = CharFilter(field_name = 'name', lookup_expr = 'icontains',)
    class Meta:
        model = models.Publisher
        fields = ('name',)

class PublisherViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):

    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherDetailSerializer
    serializer_action_classes = {'list': serializers.PublisherListSerializer,}
    permission_classes = [IsAdminOrReadOnly, permissions.IsAuthenticated,]

    
    filter_class = PublisherFilter
    search_fields = ['^name']
    ordering_fields = ('name',)  

class GenreFilter(FilterSet):
    name = CharFilter(field_name = 'name', lookup_expr = 'icontains',)
    class Meta:
        model = models.Genre
        fields = ('name',)

class GenreViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):

    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreDetailSerializer
    serializer_action_classes = {'list': serializers.GenreListSerializer,}
    permission_classes = [IsAdminOrReadOnly, permissions.IsAuthenticated,]

    #Both filters work well
    filter_class = GenreFilter
    search_fields = ['^name']
    ordering_fields = ('name',)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend,) #Controls filter ordering

class BookFilter(PropertyFilterSet):
    name = CharFilter(field_name = 'name', lookup_expr = 'icontains',)
    author = CharFilter(field_name = 'authors__name', lookup_expr = 'icontains',)
    authors = AllValuesFilter(field_name = 'authors__name',)
    genre = AllValuesFilter(field_name = 'genre__name',)
    publisher = AllValuesFilter(field_name = 'publisher__name',)
    from_pub_date = DateTimeFilter(field_name = 'pub_date', lookup_expr = 'gte')
    to_pub_date = DateTimeFilter(field_name = 'pub_date', lookup_expr = 'lte')
    price = NumberFilter(field_name = 'price', lookup_expr = 'icontains',)
    isbn = CharFilter(field_name = 'isbn', lookup_expr = 'exact',)
    total_qty = PropertyNumberFilter(field_name = 'total_qty', lookup_expr = 'gte',)
    avail_qty = PropertyNumberFilter(field_name = 'avail_qty', lookup_expr = 'gte',)
    rating = PropertyNumberFilter(field_name = 'rating', lookup_expr = 'gte',)

    class Meta:
        model = models.Book
        fields = ('name','author','authors','genre','publisher','from_pub_date','to_pub_date',
                    'price','isbn','total_qty','avail_qty','rating',)

class BookViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):

    queryset = models.Book.objects.all()
    serializer_class = serializers.BookDetailSerializer
    serializer_action_classes = {'list': serializers.BookListSerializer}
    permission_classes = [IsAdminOrReadOnly, permissions.IsAuthenticated,]

    filter_class = BookFilter 
    search_fields = ['^name','^authors__name', '^publisher__name'] 
    ordering_fields = ('name','authors__name','rating','publisher__name','genre__name','pub_date',
                        'price','total_qty','avail_qty',) 
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend,) 


    def create(self,request, *args, **kwargs):
        data = request.data

        new_book = models.Book.objects.create(name = data["name"], publisher = models.Publisher.objects.get(id = data["publisher"]),
                                            pub_date = data["pub_date"],
                                            price = data["price"],
                                            isbn = data['isbn'],)
        new_book.save()
        
        for author in data['authors']:
            author_obj = models.Author.objects.get(name = author['name'])
            new_book.authors.add(author_obj)

        for gen in data['genre']:
            gen_obj = models.Genre.objects.get(name = gen['name'])
            new_book.genre.add(gen_obj)

        serializer = serializers.BookListSerializer(new_book)
        
        return Response(serializer.data)

class BorrowedFilter(FilterSet):
    from_borrowed_date = DateTimeFilter(field_name = 'borrowed_date', lookup_expr ='gte',)
    to_borrowed_date = DateTimeFilter(field_name = 'borrowed_date', lookup_expr = 'lte',)
    from_returned_date = DateTimeFilter(field_name = 'returned_date', lookup_expr = 'gte',)
    to_returned_date = DateTimeFilter(field_name = 'returned_date', lookup_expr = 'lte',)
    has_returned = BooleanFilter(field_name = 'has_returned',)
    book_name = CharFilter(field_name = 'name__name', lookup_expr = 'icontains',label = 'book name')
    who_borrowed = CharFilter(field_name = 'who_borrowed__username', lookup_expr = 'icontains',)
    
    class Meta:
        model = models.Borrowed
        fields = ('from_borrowed_date','to_borrowed_date', 'from_returned_date',
                 'to_returned_date','has_returned','book_name','who_borrowed',)

class BorrowedViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BorrowedSerializer
    permission_classes = [IsAdminOrReadOnly, permissions.IsAuthenticated,]
    filter_class = BorrowedFilter #Everythings calm
    search_fields = ('^who_borrowed__username','^name__name',)
    ordering_fields = ('who_borrowed__username','name__name','has_returned','borrowed_date','returned_date',)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend,)

    def get_queryset(self): #Query set filters according to being a staff, staff gets all users.
                            #User gets only himself

        if self.request.user.is_staff:
            queryset = models.Borrowed.objects.all()
        
        else:
            queryset = models.Borrowed.objects.filter(who_borrowed = self.request.user.id)
        
        return queryset    

class RatingFilter(FilterSet):
    rating = NumberFilter(field_name = 'rating', lookup_expr = 'exact',)
    book_rated = CharFilter(field_name = 'book_rated__name', lookup_expr = 'icontains',)
    who_rated = CharFilter(field_name = 'who_rated__username', lookup_expr = 'icontains',)
    class Meta:
        model = models.Rating
        fields = ('rating', 'book_rated','who_rated',)

class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RatingSerializer
    
    filter_class = RatingFilter #Everything's calm
    search_fields = ('^book_rated__name','^who_rated__username',)
    ordering_fields = ('book_rated__name', 'rating', 'who_rated__username',)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)

    def get_queryset(self):  #Filter ratings so user sees only his own rating.
        if self.request.user.is_staff:
            queryset = models.Rating.objects.all()
        
        else:
            queryset = models.Rating.objects.filter(who_rated = self.request.user.id)
        
        return queryset 


class QuantityBFilter(PropertyFilterSet):
    who_ = CharFilter(field_name = 'who__username', lookup_expr = 'icontains',)
    time_left = PropertyDurationFilter(field_name = 'time_left',lookup_expr = 'gte',)
    books_borrowed = PropertyCharFilter(field_name = 'books_borrowed',lookup_expr = 'icontains',)
    quantity_borrowed = PropertyNumberFilter(field_name = 'quantity_borrowed', lookup_expr = 'gte',)
    class Meta:
        model = models.Quantity_Borrowed
        fields = ('who','time_left','books_borrowed','quantity_borrowed',)


class QuantityTimeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuantityBorrowedSerializer
    filter_class = QuantityBFilter
    def get_queryset(self):  #Filter query set so user sees only what he borrowed unless admin user
        if self.request.user.is_staff:
            queryset = models.Quantity_Borrowed.objects.all()
        
        else:
            queryset = models.Quantity_Borrowed.objects.filter(who= self.request.user.id)
        
        return queryset
    
    
        
    