from django.contrib import admin
from .models import CategoryModel
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category',)}
    list_display = ['category', 'slug']

admin.site.register(CategoryModel, CategoryAdmin)
