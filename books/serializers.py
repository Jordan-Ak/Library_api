from rest_framework import serializers
from django.contrib.auth import get_user_model
from books import models

class UserSerializer(serializers.ModelSerializer):
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
    authors = serializers.SlugRelatedField(many = True,
                                                queryset = models.Author.objects.all(), slug_field = 'name',) #To represent the relationship as a string instead of id
    genre = serializers.SlugRelatedField(many = True,
                                                 queryset = models.Genre.objects.all(),slug_field = 'name')
    
   
    class Meta:
        model = models.Book
        fields = ('name','authors','rating', 'genre')

class BookDetailSerializer(serializers.ModelSerializer):
    publisher = serializers.PrimaryKeyRelatedField(
                queryset = models.Publisher.objects.all(),source = 'publisher.name') #To display publisher name instead of id
    
    authors = serializers.StringRelatedField(many = True,) #To represent the relationship as a string instead of id
    genre = serializers.StringRelatedField(many = True,)

    class Meta:
        model = models.Book
        fields = ('name', 'authors', 'rating','genre',
                  'publisher', 'total_qty', 'avail_qty',
                  'pub_date','isbn','price',)

class BorrowedSerializer(serializers.ModelSerializer):
    who_borrowed = serializers.PrimaryKeyRelatedField(queryset = get_user_model().objects.all()
    ,source = 'who_borrowed.username')
    name = serializers.PrimaryKeyRelatedField(queryset = models.Book.objects.all(),
                                             source = 'name.name')

    class Meta:
        model = models.Borrowed
        fields = ('who_borrowed','name','has_returned','borrowed_date','returned_date',)

class RatingSerializer(serializers.ModelSerializer):
    who_rated = serializers.PrimaryKeyRelatedField(source = 'who_rated.username',
                                                    queryset = get_user_model().objects.all())
    book_rated = serializers.PrimaryKeyRelatedField(source = 'book_rated.name',
                                                     queryset = models.Book.objects.all())

    class Meta:
        model = models.Rating
        fields = ('book_rated', 'who_rated', 'rating',)

class QuantityBorrowedSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Quantity_Borrowed
        fields = ('books_borrowed_and_time_left','quantity_borrowed',)