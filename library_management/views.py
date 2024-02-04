from categories.models import CategoryModel
from books.models import BookModel
from django.shortcuts import render

def home(request, cat_slug=None):
    book_obj = BookModel.objects.all()
    if cat_slug is not None:
        cat_obj = CategoryModel.objects.get(slug=cat_slug)
        book_obj = BookModel.objects.filter(category=cat_obj)
    cat_obj = CategoryModel.objects.all()
    return render(request, 'home.html', {'cat_data':cat_obj, 'books':book_obj})

def detail(request, id):
    book = BookModel.objects.get(id=id)
    return render(request, 'book_detail.html', {'book':book})
