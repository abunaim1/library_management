from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name="home"),
    path('details/<int:id>', views.detail , name="detail"),
    path('cat_slug/<slug:cat_slug>', views.home , name="cat_slug"),
    path('user/', include('user.urls')),
    path('borrow_books/', include('borrow_books.urls')),
    path('books/', include('books.urls')),
    path('category/', include('categories.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)