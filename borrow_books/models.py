from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BorrowModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'borrow_user', null=True)
    borrow_price = models.IntegerField(null=True, blank=True)
    book_id = models.IntegerField(null=True, blank=True)
    book_title = models.CharField(max_length=50,null=True, blank=True)
    