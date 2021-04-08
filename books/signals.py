from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db.models import IntegerField
from django.db.models import F
from .models import Borrowed, Quantity_Borrowed
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
def borrowing_limit(sender, instance, **kwargs):
    current = instance
    borrowed_person = Borrowed.objects.filter(who_borrowed = current.who_borrowed)
    num_borrowed = len(borrowed_person)
    if num_borrowed > 3:
        raise Exception('Cannot borrow more than limit')


        
        
        