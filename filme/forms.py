from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms


class CriarContaForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=150, required=True)
    password1 = forms.CharField(
        label="Senha", widget=forms.PasswordInput, required=True
    )
    password2 = forms.CharField(
        label="Confirme a senha", widget=forms.PasswordInput, required=True
    )

    class Meta:
        model = Usuario
        fields = ("username", "email", "password1", "password2")


class FormHome(forms.Form):
    email = forms.EmailField(label="Email", required=False)
