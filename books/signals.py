from datetime import datetime, timedelta, timezone
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db.models import IntegerField
from django.db.models import F
from .models import Borrowed, Quantity_Borrowed, Quantity_Book
from .ad_variables import days_to_return

@receiver(pre_save, sender= Borrowed,)    #Signal for modifying returned date when user returns book
def modify_has_returned_date(sender, instance, **kwargs):
    current = instance
    try:
        previous = Borrowed.objects.get(id = instance.id)
    except ObjectDoesNotExist:
        pass
    else:
        if current.has_returned != previous.has_returned:
            instance.returned_date = datetime.now()

@receiver(pre_save, sender = Borrowed,) #Signal that constraints a user not to borrow multiple copies of the same book
def same_borrowed(sender, instance, *args, **kwargs):
    current = instance
    same_borrowed = Borrowed.objects.filter(has_returned = False).filter(
                                                who_borrowed = current.who_borrowed).filter(
                                                name = current.name).exclude(id = current.id)
    #same_borrowed filters has returned, person borrowing, name of book and excludes that instance
    
    if len(same_borrowed) == 1 and current.has_returned == False:
            raise Exception("This user cannot borrow the same book!")

@receiver(pre_save, sender = Borrowed,)     #Signal that constrains a user not to borrow more than 3 books
def num_borrowed(sender, instance, *args, **kwargs):
    current = instance
    borrowed_person = Borrowed.objects.filter(
                        who_borrowed = current.who_borrowed).filter(
                            has_returned = False).exclude(id = current.id)
    num_borrowed = len(borrowed_person)
    
    if num_borrowed == 3 and current.has_returned == False:
        raise Exception("Current user cannot borrow more than 3 books!")

@receiver(pre_save, sender = Borrowed,)    #A signal that signals if a book is out of stock at the moment.
def finished_book(sender, instance, *args, **kwargs):
    current = instance
    qty = Quantity_Book.objects.get(book = current.name)
    qty_a = qty.avail_qty
   
    if qty_a == 0 and current.has_returned == False:
       raise Exception("That book has finished!")


###Saving this code
#@receiver(pre_save, sender = Quantity_Borrowed,)
#def late_return(sender, instance, *args, **kwargs):
    #current = instance
    #borrowed_time = Borrowed.objects.filter(who_borrowed = current.who).filter(has_returned = False)
    #for time in borrowed_time: #Making a list of time left to return books
        #time_format = ((time.borrowed_date + timedelta(
         #                           days =days_to_return) - datetime.now(timezone.utc)))
        #if time_format.seconds < 0:
           # raise Exception("TTTTT")
        
        