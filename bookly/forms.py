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
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ["book", "title", "review_text", "rating"]