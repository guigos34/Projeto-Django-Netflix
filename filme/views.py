from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    FormView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarContaForm, FormHome

# Create your views here.


class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHome

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse("filme:login")
        else:
            return reverse("filme:criar_conta")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("filme:homefilmes")
        return super().get(request, *args, **kwargs)


class Homefilmes(LoginRequiredMixin, ListView):
    model = Filme
    template_name = "homefilmes.html"
    context_object_name = "filmes"


class DetalhesFilme(LoginRequiredMixin, DetailView):
    model = Filme
    template_name = "detalhes_filme.html"
    context_object_name = "filme"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.qtde_views += 1
        self.object.save()
        usuario = request.user
        usuario.filmes_vistos.add(self.object)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(
            categoria=self.get_object().categoria
        ).exclude(id=self.object.id)[:3]
        context["filmes_relacionados"] = filmes_relacionados
        return context


class BuscaFilme(LoginRequiredMixin, ListView):
    model = Filme
    template_name = "busca_filme.html"
    context_object_name = "lista_filmes_busca"  # Adicione isso

    def get_queryset(self):
        query = self.request.GET.get("query")
        if query:
            return Filme.objects.filter(titulo__icontains=query)
        return Filme.objects.none()  # Melhor retornar uma lista vazia do que None


class CriarConta(FormView):
    template_name = "criar_conta.html"
    form_class = CriarContaForm

    def get_success_url(self):
        return reverse("filme:login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PaginaPerfil(LoginRequiredMixin, UpdateView):
    model = Usuario
    template_name = "perfil.html"
    fields = ["username", "email"]

    def get_success_url(self):
        return reverse("filme:homefilmes")
