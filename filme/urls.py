"""
URL configuration for Projeto6 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, reverse_lazy
from filme.views import (
    DetalhesFilme,
    Homepage,
    Homefilmes,
    BuscaFilme,
    PaginaPerfil,
    CriarConta,
)
from django.contrib.auth import views as auth_views

app_name = "filme"

urlpatterns = [
    path("", Homepage.as_view(), name="homepage"),
    path("filmes/", Homefilmes.as_view(), name="homefilmes"),
    # url diferente pra cada filme, usando a chave primaria do filme
    path("filmes/<int:pk>/", DetalhesFilme.as_view(), name="detalhes_filme"),
    path("pesquisa/", BuscaFilme.as_view(), name="busca_filme"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="logout.html"),
        name="logout",
    ),
    path("perfil/<int:pk>/", PaginaPerfil.as_view(), name="perfil"),
    path("criar-conta/", CriarConta.as_view(), name="criar_conta"),
    path(
        "mudar-senha/",
        auth_views.PasswordChangeView.as_view(
            template_name="perfil.html", success_url=reverse_lazy("filme:homefilmes")
        ),
        name="mudar-senha",
    ),
]
