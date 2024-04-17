from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout 
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from bookly.forms import RegisterForm, ReviewForm
from .models import Reviews, Books
from django.views.generic import ListView
from django.contrib.auth.views import LoginView
from .forms import MyAuthForm


#Página de login do usuário com formulário de login personalizado
class User(LoginView):
    authentication_form = MyAuthForm
    model = User

#Página para registro de novos usuários (apenas para super usuários)
@login_required(login_url="/login")
def registrate_users(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('bookly:index')
    else:
        form = RegisterForm()

    return render(request, 'registration/registrate_users.html', {"form": form})

#Logout do usuário 
@login_required(login_url="/login")
def user_logout(request):
    logout(request)
    return redirect('/login')


class BookListView(ListView):
    model = Books
    template_name = 'books/books_list.html'
    context_object_name='books_list'
    queryset = Books.objects.all()

class BooksSearchView(ListView):
    model = Books
    template_name = 'books/books_list.html'
    context_object_name='books_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query :
            query = ""
        return Books.objects.filter(title__icontains=query).order_by('-title')

def books_list(request):
    return render(request, '/books', {
        "title": "Livros disponíveis",
        "message": "Busque pelo livro que deseja!",
    })

# @login_required(login_url="/login")
def home(request):
    reviews = Reviews.objects.all()

    if request.method == "POST":
        review_id = request.POST.get("review-id")
        user_id = request.POST.get("user-id")
        print(user_id)

        if review_id:
            review = Reviews.objects.filter(id = review_id).first()
            if review and (review.user == request.user or request.user.has_perm("bookly.delete_reviews")):
                review.delete()
        elif user_id:
            user = User.objects.filter(id = user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass

    return render(request, 'bookly/index.html', {"reviews": reviews})

@login_required(login_url="/login")
@permission_required("bookly.add_reviews", login_url="/login", raise_exception=True)
def create_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("/index")
    else:
        form = ReviewForm()

    return render(request, "bookly/create_review.html", {"form": form})

