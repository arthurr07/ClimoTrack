from django.shortcuts import render
from app.models import DadosHidricos, Cidade
def index(request):
    list = Cidade.objects.all()
    return render(request, 'index.html', {'list':list})

def table(request): 
    city = request.GET.get('cidade')
    list = DadosHidricos.objects.all().filter(cidade=city)
    return render(request, 'tabela.html', {'list':list})
# Create your views here.
