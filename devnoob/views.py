from django.shortcuts import render,redirect
from devnoob.models import Habilidade
from devnoob.models import Portfolio
from devnoob.models import Caracteristica
from devnoob.models import Gosto
from devnoob.models import Recomendacao
from devnoob.models import Perfil
from devnoob.forms import HabiliadeForm
# Create your views here.
def home (request):
    lista_habilidades = Habilidade.objects.all()
    lista_portfolio = Portfolio.objects.all()
    lista_caracteristicas = Caracteristica.objects.all()
    lista_gostos = Gosto.objects.all()
    lista_recomendacoes = Recomendacao.objects.all()
    lista_perfil = Perfil.objects.all()
    listas = {
    'lista_habilidades':lista_habilidades ,
    'lista_portfolio' :lista_portfolio ,
    'lista_caracteristicas' : lista_caracteristicas ,
    'lista_gostos' : lista_gostos ,
    'lista_recomendacoes' : lista_recomendacoes ,
    'lista_perfil' : lista_perfil
    }
    return render(request,'devnoob/index.html', listas)
def cadastro(request):
    form = HabiliadeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(home)
    return render(request,'devnoob/cadastro.html',{'form': form})
