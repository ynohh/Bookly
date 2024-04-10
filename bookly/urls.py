from django.urls import path

from . import views

app_name = "bookly"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]