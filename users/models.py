from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class CustomUser(AbstractUser): #Current model for custom user
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = CharField(max_length = 100, blank=False, null = False)
    last_name = CharField(max_length = 100, blank=False, null = False)
    email = models.EmailField(max_length = 254, blank = False, null = False, unique = True,)
    phone_no = models.CharField(max_length = 30, blank=True, null=True,)