from rest_framework import serializers
from django.contrib.auth import get_user_model
from books import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username','email',)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ('name')

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = ('name')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ()