from django.shortcuts import render
from app.models import Cidade
def index(request):
    list = Cidade.objects.all()
    return render(request, 'index.html', {'list':list})

def table(request): 
    city = request.GET.get('cidade')
    #list = Precipitacao.objects.all().filter(cidade=city)
    #return render(request, 'tabela.html', {'list':list})
    return render(request, 'tabela.html')
# Create your views here.
