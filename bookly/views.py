from django.shortcuts import render, redirect
from django.contrib.auth import login, logout 
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import User, Group
from bookly.forms import RegisterForm, ReviewForm
from .models import Reviews, Books
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from .forms import MyAuthForm
from django.contrib.auth.mixins import LoginRequiredMixin

#home page
@login_required(login_url="/login")
def home(request):
    return render(request, 'bookly/index.html', {"reviews": reviews})

class User(LoginView):
    authentication_form = MyAuthForm
    model = User

#cadastro do usuário
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('bookly:login')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})    


#Logout do usuário 
@login_required(login_url="/login")
def user_logout(request):
    logout(request)
    return redirect('/login')

#Listagem dos livros
class BookListView(LoginRequiredMixin, ListView):
    model = Books
    template_name = 'books/books.html'
    context_object_name='books_list'
    queryset = Books.objects.all()
    
    def get_queryset(self):
        selectedOpt = self.request.GET.get('dropdown')
        if selectedOpt == None:
            selectedOpt = 'title'

        query = self.request.GET.get('searched')
        if not query:
            query = ""

        if selectedOpt == 'title':
            return Books.objects.filter(title__icontains=query).order_by('title')
        elif selectedOpt == 'author':
            return Books.objects.filter(author__icontains=query).order_by('author')  
        elif selectedOpt == 'genre':
            return Books.objects.filter(genre__icontains=query).order_by('genre')


class BooksDetailView(DetailView):
    model = Books

#Listagem das resenhas do livro selecionado
@login_required(login_url="/login")
def reviews(request, book_id):
    reviews = Reviews.objects.filter(book_id = book_id).order_by('-created_at')
    current = Books.objects.get(id = book_id)
    form = ReviewForm(request.POST)
    
    if request.method == "POST":
        review_id = request.POST.get("review-id")
        user_id = request.POST.get("user-id")

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = current
            review.save()
            return redirect("/books/reviews/{}".format(book_id))
        else:
            form = ReviewForm()

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
    context = {
        "reviews": reviews,
        "form": form
    }
    return render(request, 'bookly/reviews.html', context)

# @login_required(login_url="/login")
# @permission_required("bookly.add_review", login_url="/login", raise_exception=True)
# def create_review(request, book_id):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         current_book = Books.objects.filter(id = book_id).first()

#         if form.is_valid():
#             review = form.save(commit=False)
#             review.user = request.user
#             review.book = current_book
#             review.save()
#             return redirect("/books/reviews/{}".format(book_id))
#     else:
#         form = ReviewForm()
