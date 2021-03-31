from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.name.title()

class Book(models.Model):
    name = models.CharField(max_length = 150,)
    authors = models.CharField(max_length = 100, null = False, blank = False)
    genre = models.ManyToManyField(Genre)
    publisher = models.CharField(max_length = 100)
    pub_date = models.DateField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    ratings = models.FloatField()
    isbn = models.CharField(max_length = 13, unique = True, default ='NULL')
    total_qty = models.IntegerField()
    avail_qty = models.IntegerField()

    def __str__(self):
        return self.name.title()

    

class Borrowed(models.Model):
    name = models.ForeignKey(Book, on_delete = models.CASCADE,)
    borrowed_date = models.DateTimeField(auto_now_add = True)
    has_returned = models.BooleanField(default = False)
    returned_date = models.DateTimeField(auto_now = True)
    who_borrowed = models.ForeignKey(get_user_model(), on_delete = models.SET_DEFAULT, default = '71ba608e-20ed-4954-89e3-942a03e6327d')

    class Meta:
        verbose_name_plural = 'Borrowed'

    def __str__(self):
        return self.name.title()

    



