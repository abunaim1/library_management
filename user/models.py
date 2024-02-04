from django.db import models
from django.contrib.auth.models import User
from books.models import BookModel
# Create your models here.

class AccountModel(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete = models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.user}'

class Review(models.Model):
    user = models.ForeignKey(User, related_name='review_user', on_delete = models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete = models.CASCADE, null=True, blank=True)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

