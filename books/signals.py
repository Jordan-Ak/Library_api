from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db.models import IntegerField
from django.db.models import F
from .models import Borrowed, Quantity_Borrowed, Quantity
from django.utils import timezone

@receiver(pre_save, sender= Borrowed,)
def modify_has_returned_date(sender, instance, **kwargs):
    current = instance
    try:
        previous = Borrowed.objects.get(id = instance.id)
    except ObjectDoesNotExist:
        pass
    else:
        if current.has_returned != previous.has_returned:
            instance.returned_date = timezone.now()

@receiver(pre_save, sender = Borrowed,)
def same_borrowed(sender, instance, *args, **kwargs):
    current = instance
    same_borrowed = Borrowed.objects.filter(has_returned = False).filter(
                                                who_borrowed = current.who_borrowed).filter(
                                                name = current.name   
                                                )
    if len(same_borrowed) == 1:
            raise Exception("This user cannot borrow the same book!")

@receiver(pre_save, sender = Borrowed,)
def num_borrowed(sender, instance, *args, **kwargs):
    current = instance
    borrowed_person = Borrowed.objects.filter(who_borrowed = current.who_borrowed)
    num_borrowed = len(borrowed_person)
    
    if num_borrowed == 3 and current.has_returned == False:
        raise Exception("Current user cannot borrow more than 3 books!")

@receiver(pre_save, sender = Borrowed,)
def finished_book(sender, instance, *args, **kwargs):
    current = instance
    qty = Quantity.objects.get(book = current.name)
    qty_a = qty.avail_qty
   
    if qty_a == 0 and current.has_returned == False:
       raise Exception("That book has finished!")

        
        
        