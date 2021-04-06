from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Borrowed
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
        
        
        