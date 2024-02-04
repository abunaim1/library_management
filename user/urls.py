from django.urls import path
from . import views
urlpatterns = [
    # path('deposite/', views.deposite, name='deposte')
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('deposite/', views.deposite, name='deposite'),
    path('borrow/<int:book_id>/', views.borrow, name='borrow'),
    path('profile/', views.profile, name='profile'),
    path('review/<int:book_id>/', views.review, name='review'),
    path('return/<int:book_id>/', views.return_book, name='return'),
]
