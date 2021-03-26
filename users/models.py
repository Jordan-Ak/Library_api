from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    first_name = models.CharField(max_length = 100, blank=False, null = False,verbose_name='first name',)
    last_name = models.CharField(max_length = 100, blank=False, null = False,verbose_name='last name',)
    email = models.EmailField(max_length = 254, blank = False, null = False, unique = True,)
    phone_no = models.CharField(max_length = 30, blank=True, null=True,)