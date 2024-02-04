from django.db import models
from borrow_books.models import BorrowModel
from categories.models import CategoryModel
# Create your models here.

class BookModel(models.Model):
    borrow_books = models.ForeignKey(BorrowModel, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ManyToManyField(CategoryModel)
    image = models.ImageField(upload_to='books/media/uploads/')
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

