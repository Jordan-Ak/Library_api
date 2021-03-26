from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(max_length = 254, required =True, unique = True,)
    phone_no = models.CharField(max_length = 30, blank=True, null=True,)