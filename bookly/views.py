from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.template import loader
from django.http import JsonResponse
from .models import Livros

class IndexView(generic.ListView):
    template_name = "bookly/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Livros.objects.order_by("-id_livro")[:1]

class ListView(generic.ListView):
    template_name = 'bookly/list_view.html'
    model = Livros
