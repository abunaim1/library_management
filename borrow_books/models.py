from django.db import models

# Create your models here.
class BorrowModel(models.Model):
    borrow_price = models.IntegerField()
    is_borrow = models.BooleanField()