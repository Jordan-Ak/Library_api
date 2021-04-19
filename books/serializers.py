from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from django.contrib.auth import get_user_model
from books import models

class UserSerializer(serializers.ModelSerializer):
    date_joined =  serializers.DateTimeField(format = "%H:%M, %d-%m-%Y")
    class Meta:
        model = get_user_model()
        fields = ('id','username','email','date_joined',)

class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ('name',)

class AuthorDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Author
        fields = ('name','books',)



class PublisherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = ('name',)

class PublisherDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Publisher
        fields = ('name', 'books')

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = ('name',)

class GenreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = ('name', 'books',)


class BookListSerializer(serializers.ModelSerializer):
    #authors = AuthorListSerializer(many = True,) #To represent the relationship as a string instead of id
    #genre = serializers.SlugRelatedField(many = True,
     #                                            queryset = models.Genre.objects.all(),slug_field = 'name')
    
   
    class Meta:
        model = models.Book
        fields = ('name', 'authors', 'rating','genre',
                  'publisher', 'total_qty', 'avail_qty',
                  'pub_date','isbn','price',)
        depth = 1

class BookDetailSerializer(serializers.ModelSerializer):
    #publisher = serializers.SlugRelatedField(
     #           queryset = models.Publisher.objects.all(), slug_field= 'name') #To display publisher name instead of id
    
    #authors = serializers.StringRelatedField(many = True,) #To represent the relationship as a string instead of id
    #genre = serializers.StringRelatedField(many = True,)

    class Meta:
        model = models.Book
        fields = ('name', 'authors', 'rating','genre',
                  'publisher', 'total_qty', 'avail_qty',
                  'pub_date','isbn','price',)
        depth = 1

class BorrowedSerializer(serializers.ModelSerializer):
    who_borrowed = serializers.SlugRelatedField(queryset = get_user_model().objects.all(),
                                                slug_field = 'username')
    name = serializers.SlugRelatedField(queryset = models.Book.objects.all(),
                                             slug_field = 'name')

    borrowed_date = serializers.DateTimeField(format = "%H:%M, %d-%m-%Y", read_only = True)
    #returned_date = serializers.DateTimeField(format = "%H:%M, %d-%m-%Y", )

    class Meta:
        model = models.Borrowed
        fields = ('who_borrowed','name','has_returned','borrowed_date','returned_date',)

    def to_representation(self, instance):  #This defines how returned date is to be displayed, if value is null display default
        representation = super(BorrowedSerializer, self).to_representation(instance)
        try:
            representation['returned_date'] = instance.returned_date.strftime("%H:%M, %d-%m-%Y")
        except AttributeError:
            return representation

        return representation

class RatingSerializer(serializers.ModelSerializer):
    who_rated = serializers.SlugRelatedField(slug_field = 'username',
                                                    queryset = get_user_model().objects.all())
    book_rated = serializers.SlugRelatedField(slug_field = 'name',
                                                     queryset = models.Book.objects.all())

    class Meta:
        model = models.Rating
        fields = ('book_rated', 'who_rated', 'rating',)

class QuantityBorrowedSerializer(serializers.ModelSerializer):
    who = serializers.SlugRelatedField(slug_field = 'username',
                                 queryset = get_user_model().objects.all())
    
    class Meta:
        model = models.Quantity_Borrowed
        fields = ('who','books_borrowed','time_left','quantity_borrowed',)
