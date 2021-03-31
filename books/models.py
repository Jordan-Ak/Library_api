from django.db import models
from django.contrib.auth import get_user_model()
# Create your models here.

class Genre(models.Model):
    name = CharField(max_length = 50)

class Book(models.Model):
    name = models.CharField(max_length = 150,)
    author(s) = models.CharField(max_length = 100, null = False, blank = False)
    genre = models.ManytoManyField(Genre)
    publisher = models.CharField(max_length = 100)
    pub_date = models.DateField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    ratings = models.FloatField()
    total_qty = models.IntegerField()
    avail_qty = models.InterField()
    
    def __str__(self):
        return self.name.title()

    

class Borrowed(models.Model):
    name = models.ForeignKey(Book, )
    borrowed_date = models.DateTimeField(auto_now_add = True)
    has_returned = models.BooleanField(default = False)
    returned_date = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = 'Borrowed'

    def __str__(self):
        return self.name.title()

    



