# context.py gerencia todas as variáveis de contexto que serão usadas nos templates. Ele é responsável por fornecer dados para os templates, como listas de filmes, detalhes de um filme específico, etc. O context.py é onde você pode definir funções ou classes que retornam dicionários de contexto para serem usados em seus templates. Ele é uma parte importante do processo de renderização dos templates, pois permite que você passe dados dinâmicos para eles.

from .models import Filme


def lista_filmes_recentes(request):
    filmes = Filme.objects.order_by("-data_criacao")[:8]
    return {"filmes_recente": filmes}


def filmes_destaque(request):
    filmes = Filme.objects.order_by("-qtde_views")[:8]
    return {"filmes_destaque": filmes}


def filme_destaque(request):
    filme = Filme.objects.order_by("-qtde_views").first()
    if filme:
        return {"filme_destaque": filme}
    else:
        return {"filme_destaque": None}
