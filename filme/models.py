from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


LISTA_CATEGORIAS = [
    ("acao", "Ação"),
    ("aventura", "Aventura"),
    ("comedia", "Comedia"),
    ("romance", "Romance"),
    ("drama", "Drama"),
    ("terror", "Terror"),
    ("fantasia", "Fantasia"),
    ("familia", "Familia"),
    ("suspense", "Suspense"),
    ("ficcao", "Ficção Científica"),
    ("animacao", "Animação"),
    ("documentario", "Documentário"),
]


class Filme(models.Model):
    thumb = models.ImageField(upload_to="thumb_filmes/")
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    qtde_views = models.IntegerField(default=0)
    data_criacao = models.DateField(default=timezone.now)

    def __str__(self):
        return self.titulo


class Episodio(models.Model):
    filme = models.ForeignKey(
        "Filme", on_delete=models.CASCADE, related_name="episodios"
    )
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return f"{self.filme.titulo} - {self.titulo}"


class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("filme.Filme", blank=True)
