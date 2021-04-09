from datetime import datetime, timedelta, timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Avg, F
from django.core.validators import MaxValueValidator, MinLengthValidator
 

# Create your models here.

class Author(models.Model): #Author of books
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name.title()

class Publisher(models.Model): #Publihsers of books
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name.title()

class Genre(models.Model): #Genre of books
    name = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.name.title()



class Book(models.Model):
    name = models.CharField(max_length = 150,)   #Name of books
    authors = models.ManyToManyField(Author)     #Many to many because multiple books can have multiple authors
    genre = models.ManyToManyField(Genre)       #Many to many because multiple genres can appear on multiple books
    publisher = models.ForeignKey(Publisher, null = True, blank = True, on_delete = models.CASCADE) 
    #A book should have a publisher will include a none field for books without publishers
    
    pub_date = models.DateField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2) #Price of book incase user misplaces it
    isbn = models.CharField(max_length = 13, unique = True, null = True, blank = True,
                            validators = [MinLengthValidator(13)]) 
                            #ISBN numbers can't be less or more than 13 numbers
    
    
    @property # Code to get total quantity of books for a particular book # reference from a class futher down
    def total_qty(self):
        total = Quantity.objects.get(book = self.id)
        qty_t = total.total_qty
        return qty_t

    @property #Code to obtain available quantity of books remaining after books have been borrowed
    def avail_qty(self):
        qty = Quantity.objects.get(book = self.id)
        qty_a = qty.avail_qty
        return qty_a

    @property #Code to determine average rating from users
    def rating_book(self):
        avg_rating = Rating.objects.filter(book_rated = self.id).aggregate(Avg('rating'))
        return avg_rating['rating__avg']
    
    def __str__(self):
        return self.name.title()

class Borrowed(models.Model):    #Model for users borrowing and returning
    name = models.ForeignKey(Book, on_delete = models.CASCADE,)
    borrowed_date = models.DateTimeField(auto_now_add = True)   #Date is created as soon as instance is created
    has_returned = models.BooleanField(default = False)    #Field that determines if a model is returend or not
    returned_date = models.DateTimeField(null = True, blank = True,)    #Date that changes as soon as book is returned
    who_borrowed = models.ForeignKey(get_user_model(), on_delete = models.SET_DEFAULT, default ='9c495b90-3900-43d1-875d-6b15d5d5ab55')
               
    class Meta:
        verbose_name_plural = 'Borrowed' #Name for plural object that displays in admin
        
    def __str__(self):
        return self.name.name.title() + ', ' + self.who_borrowed.username

class Rating(models.Model):     #Rating for books
    who_rated = models.ForeignKey(get_user_model(), on_delete =models.CASCADE,)
    book_rated = models.ForeignKey(Book, on_delete = models.CASCADE,)
    rating = models.PositiveIntegerField(validators = [MaxValueValidator(5)])  #Rating shouldn't be higher than 5

    class Meta: #This constraint restricts users to have only one rating per book
        unique_together = ('who_rated', 'book_rated',)
    
    def __str__(self):
        return self.book_rated.name.title() + ', ' + self.who_rated.username

class Quantity(models.Model):     #Quantity of books for a particular book
    book = models.OneToOneField(Book, on_delete = models.CASCADE)  #One book to one quantity
    total_qty = models.PositiveIntegerField()
    
    @property
    def avail_qty(self): #This code calculates the quantity of books available for lending
        taken = Borrowed.objects.filter(has_returned__exact = False).filter(name = self.book)
        taken_qty = (len(taken))
        qty = self.total_qty - taken_qty
        return qty 
    
    class Meta:
        verbose_name_plural = 'Quantities'

    def __str__(self):
        return self.book.name.title()

class Quantity_Borrowed(models.Model):    #Amount a user has borrowed
    who = models.ForeignKey(get_user_model(), on_delete = models.CASCADE,)

    @property #This is code to determine which books this user borrowed
    def books_borrowed(self):
        borrowed_person = Borrowed.objects.filter(who_borrowed = self.who).filter(has_returned = False)
        books = []
        for borrowed_book in borrowed_person:
            books.append(borrowed_book.name.name.title())
        return ','.join(map(str,books))  #Returns a list of books separated by a comma.
    
    @property #This code is to ascertain time limit for book returned
    def time_left(self):
        borrowed_time = Borrowed.objects.filter(who_borrowed = self.who).filter(has_returned = False)
        left_time = []
        for time in borrowed_time:
            left_time.append((time.borrowed_date + timedelta(days =14)- datetime.now(timezone.utc)))    
            
            #left_time.append(time.borrowed_date)
        return str(left_time)


    @property #This is code to determine how many books that has been borrowed by a user
    def quantity_borrowed(self):
        borrowed_person = Borrowed.objects.filter(who_borrowed = self.who).filter(has_returned = False)
        num_borrowed = len(borrowed_person)
        return num_borrowed
    
    
    class Meta:
        verbose_name_plural = 'Quantity_Borrowed'
   
    def __str__(self):
        return self.who.username
            
        

######  Code I might use later    
#class Total_Quantity(models.Model):

   # def total_qty_borrowed(self):
     #   taken_qty = Borrowed.objects.filter(has_returned__exact = False)
      #  return(len(taken_qty))
        
    #def total_qty_books(self):
     #   books = Quantity.objects.all()

      #  for i in range (len(books)):
           # total =+ Quantity.objects.get(id = i).total_qty
       #     return total

    #class Meta:
     #   verbose_name_plural = 'Total Quantities'

#def total_qty_borrowed(self):
        #taken_qty = Borrowed.objects.filter(has_returned__exact = False)
        #return(len(taken_qty)) 
    
    