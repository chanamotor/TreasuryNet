from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    user_type = models.CharField(max_length=20, default='admin')
    mob_no = models.CharField(max_length=10, blank=True)
    status = models.BooleanField(default=False)