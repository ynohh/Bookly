from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Reviews
from django.forms.widgets import PasswordInput, TextInput
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

class MyAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Usuário'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Senha'}))
    error_messages = {
        'invalid_login': _(mark_safe("Invalid credentials!")
        ),
        'inactive': _("This account is inactive."),
    }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='E-mail:',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'E-mail',
                'class': 'form-control',
            }
        )
    )   

    username = forms.CharField(
        label='Nome de usuário',
        widget=TextInput(
            attrs={
                'placeholder': 'Nome de usuário',
                'class': 'form-control',
            }
        )
    )

    password1 = forms.CharField(
        label='Senha',
        widget=PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Senha',
            }     
        )
    )

    password2 = forms.CharField(
        label='Confirmar senha',
        widget=PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Confirme a senha',
            }     
        )
    )



    error_messages = {
        'invalid_login': _(mark_safe("Invalid credentials!")
        ),
        'inactive': _("This account is inactive."),
    }
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ReviewForm(forms.ModelForm):
    rating_choices = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )

    rating = forms.ChoiceField(
        label = "Qual nota você dá para o livro?",
        choices = rating_choices,
        widget = forms.RadioSelect(
            attrs={
                'class':'form-control rating',
            }
        )
    )

    title = forms.CharField(
        label = 'Título da resenha:',
        widget = TextInput(
            attrs={ 
                'class':'form-control title', 
                'placeholder':'Dê um título para sua resenha'
            }
        )
    )
    review_text = forms.CharField(
        label = "Escreva sua avaliação:",
        widget = forms.Textarea(
            attrs={
                'class':'form-control review-text', 
                'placeholder':'No geral, o que você achou do livro?',
                'maxlength': '1000',
            }
        )
    )
    
    class Meta:
        model = Reviews
        fields = ["title", "review_text", "rating"]