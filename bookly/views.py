from django.shortcuts import render
from django.views import generic
from .models import Livros
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from bookly.forms import LoginForm

class IndexView(generic.ListView):
    template_name = "bookly/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Livros.objects.order_by("-id_livro")[:1]

#Página de login
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'bookly/login.html', {'form': form})

#Página de logout
def user_logout(request):
    logout(request)
    return redirect('bookly:login')