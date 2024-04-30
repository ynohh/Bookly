from django.urls import path
from . import views
from .models import Books

app_name = "bookly"
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.User.as_view(), name="login"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path("user_logout/", views.user_logout, name="user_logout"),
    path('books/', views.BookListView.as_view(), name='books'),
    path("books/reviews/<book_id>", views.reviews, name="reviews"),
    path('books/<pk>/', views.BooksDetailView.as_view(), name='book_detail'),
]