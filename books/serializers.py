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
    authors = serializers.StringRelatedField(many = True,) #To represent the relationship as a string instead of id
    genre = serializers.StringRelatedField(many = True,)
   
   
    class Meta:
        model = models.Book
        fields = ('name','authors','rating', 'genre')

class BookDetailSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source = 'publisher.name') #To display publisher name instead of id
    authors = serializers.StringRelatedField(many = True,) #To represent the relationship as a string instead of id
    genre = serializers.StringRelatedField(many = True,)

    class Meta:
        model = models.Book
        fields = ('name', 'authors', 'rating','genre',
                  'publisher', 'total_qty', 'avail_qty',
                  'pub_date','isbn','price',)

class BorrowedSerializer(serializers.ModelSerializer):
    who_borrowed = serializers.ReadOnlyField(source = 'who_borrowed.username')
    
    class Meta:
        model = models.Borrowed
        fields = ('who_borrowed','name','has_returned','borrowed_date','returned_date',)

class RatingSerializer(serializers.ModelSerializer):
    who_rated = serializers.PrimaryKeyRelatedField(source = 'who_rated.username',
                                                    queryset = models.Rating.objects.all())

    class Meta:
        model = models.Rating
        fields = ('book_rated', 'who_rated', 'rating',)