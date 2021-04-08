from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from django.db.models import Avg, Count
from django.core.validators import MaxValueValidator


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name.title()

class Publisher(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name.title()

class Genre(models.Model):
    name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.name.title()



class Book(models.Model):
    name = models.CharField(max_length = 150,)
    authors = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)
    publisher = models.ForeignKey(Publisher, null = True, blank = True, on_delete = models.CASCADE)
    pub_date = models.DateField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    isbn = models.CharField(max_length = 13, unique = True, null = True, blank = True,)
    
    
    @property
    def total_qty(self):
        total = Quantity.objects.get(book = self.id)
        qty_t = total.total_qty
        return qty_t

    @property
    def avail_qty(self):
        qty = Quantity.objects.get(book = self.id)
        qty_a = qty.avail_qty
        return qty_a

    @property
    def rating_book(self):
        avg_rating = Rating.objects.filter(book_rated = self.id).aggregate(Avg('rating'))
        return avg_rating['rating__avg']
    
    #@property
    #def avail_qty(self):
        #qty_a = self.total_qty 
        #return qty_a


    def __str__(self):
        return self.name.title()

class Borrowed(models.Model):
    name = models.ForeignKey(Book, on_delete = models.CASCADE,)
    borrowed_date = models.DateTimeField(auto_now_add = True)
    has_returned = models.BooleanField(default = False)
    returned_date = models.DateTimeField(null = True, blank = True,)
    who_borrowed = models.ForeignKey(get_user_model(), on_delete = models.SET_DEFAULT, default ='9c495b90-3900-43d1-875d-6b15d5d5ab55')

#def total_qty_borrowed(self):
        #taken_qty = Borrowed.objects.filter(has_returned__exact = False)
        #return(len(taken_qty))    

    class Meta:
        verbose_name_plural = 'Borrowed'
        unique_together = ('who_borrowed', 'name',)

    def __str__(self):
        return self.name.name.title()

class Rating(models.Model):
    who_rated = models.ForeignKey(get_user_model(), on_delete =models.CASCADE,)
    book_rated = models.ForeignKey(Book, on_delete = models.CASCADE,)
    rating = models.PositiveIntegerField(validators = [MaxValueValidator(5)])

    class Meta:
        unique_together = ('who_rated', 'book_rated',)
    
    def __str__(self):
        return self.book_rated.name.title()

class Quantity(models.Model):
    book = models.OneToOneField(Book, on_delete = models.CASCADE)
    total_qty = models.IntegerField()
    
    @property
    def avail_qty(self):
        taken = Borrowed.objects.filter(has_returned__exact = False).filter(name = self.book)
        taken_qty = (len(taken))
        qty = self.total_qty - taken_qty
        return qty 
    


    class Meta:
        verbose_name_plural = 'Quantities'

    def __str__(self):
        return self.book.name.title()

    
        