from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AccountModel(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    


