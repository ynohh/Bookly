from django.urls import path
from . import views
from .models import Books

app_name = "bookly"
urlpatterns = [
    path('', views.home, name='index'),
    path('index/', views.home, name='index'),
    path('login/', views.User.as_view(), name="login"),
    path('registrate_users/', views.registrate_users, name="registrate_users"),
    path("user_logout/", views.user_logout, name="user_logout"),
    path('books_list/', views.BookListView.as_view(), name='books_list'),
    path('search_books/', views.BooksSearchView.as_view(), name='search_books'),
    path("create_review/", views.create_review, name="create_review"),
]