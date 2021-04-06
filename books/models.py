from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 100)

class Publisher(models.Model):
    name = models.CharField(max_length = 100)

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
    rating_b = models.FloatField(null = True, blank = True,)
    isbn = models.CharField(max_length = 13, unique = True, default ='NULL')
    total_qty = models.IntegerField(null = True, blank = True)
    avail_qty = models.IntegerField(null = True, blank = True)

    def __str__(self):
        return self.name.title()
    
    #def rating_b(self):
        #rating = Rating.objects.filter(book_rated = Book)
    

class Borrowed(models.Model):
    name = models.ForeignKey(Book, on_delete = models.CASCADE,)
    borrowed_date = models.DateTimeField(auto_now_add = True)
    has_returned = models.BooleanField(default = False)
    returned_date = models.DateTimeField()
    who_borrowed = models.ForeignKey(get_user_model(), on_delete = models.SET_DEFAULT, default = '71ba608e-20ed-4954-89e3-942a03e6327d')

    class Meta:
        verbose_name_plural = 'Borrowed'

    def __str__(self):
        return self.name.name.title()

class Rating(models.Model):
    who_rated = models.ForeignKey(get_user_model(), on_delete =models.CASCADE)
    book_rated = models.ForeignKey(Book, on_delete = models.CASCADE)
    rating = models.FloatField()


#class Returned(models.Model):



        


    



