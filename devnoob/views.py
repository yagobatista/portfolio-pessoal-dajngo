from django.shortcuts import render,redirect
from devnoob.models import Habilidade
from devnoob.models import Portfolio
from devnoob.models import Caracteristica
from devnoob.models import Gosto
from devnoob.models import Recomendacao
from devnoob.models import Perfil
# Create your views here.
def home (request):
    lista_habilidades = Habilidade.objects.all()
    lista_portfolio = Portfolio.objects.all()
    lista_caracteristicas = Caracteristica.objects.all()
    lista_gostos = Gosto.objects.all()
    lista_recomendacoes = Recomendacao.objects.all()
    perfil = Perfil.objects.get(id=1)
    listas = {
    'lista_habilidades':lista_habilidades ,
    'lista_portfolio' :lista_portfolio ,
    'lista_caracteristicas' : lista_caracteristicas ,
    'lista_gostos' : lista_gostos ,
    'lista_recomendacoes' : lista_recomendacoes ,
    'perfil' : perfil,
    'contador':0
    }
    return render(request,'devnoob/index.html', listas)
