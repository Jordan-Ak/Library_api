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


"""
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ()
"""