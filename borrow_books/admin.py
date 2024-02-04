from django.contrib import admin
from borrow_books.models import BorrowModel
# Register your models here.

class BorrowAdmin(admin.ModelAdmin):
    list_display = ['book_id', 'user', 'book_title', 'borrow_price']

admin.site.register(BorrowModel, BorrowAdmin)