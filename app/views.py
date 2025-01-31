from django.shortcuts import render
from app.models import Cidade, DadosHidricos, Estado
def index(request):
    city_list = Cidade.objects.all()
    uf_list = Estado.objects.all()
    if request.method == "POST":
        cidade = int(request.POST['cidade'])
        data = DadosHidricos.objects.select_related().filter(estacao=cidade)
        return render(request, 'index.html', {'city_list':city_list, 'uf_list':uf_list, 'data':data})
    return render(request, 'index.html', {'city_list':city_list, 'uf_list':uf_list})
    
def table(request): 
    city = request.GET.get('cidade')
    #list = Precipitacao.objects.all().filter(cidade=city)
    #return render(request, 'tabela.html', {'list':list})
    return render(request, 'tabela.html')

def login(request):
    return render(request, 'login.html')
# Create your views here.
