from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db.models import IntegerField
from django.db.models import F
from .models import Borrowed, Quantity, Book
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

#@receiver(post_save, sender = Borrowed,)
#def modify_quantities(sender, instance, **kwargs):
    #current = instance
    #if current.has_returned == False:
        #Quantity.avail_qty = Quantity.objects.get(book = 3).annotate(
          #                      avail_qty = F(Quantity.total_qty) - 1)
        
    #else:
     #   (Quantity.avail_qty) += 1 
        
        
        