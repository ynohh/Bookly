from django.urls import path

from . import views

app_name = "bookly"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("", views.ListView.as_view(), name="list"),
]