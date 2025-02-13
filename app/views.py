from django.shortcuts import render
from app.models import Cidade, DadosHidricos, Estado
def index(request):
    city_list = Cidade.objects.all()
    uf_list = Estado.objects.all()

    if request.method == "POST":
        cidade = int(request.POST['cidade'])
        data = DadosHidricos.objects.filter(estacao=cidade).first()
        cidade_selecionada = Cidade.objects.get(id=cidade)
        
        if data:  # Se houver dados para a cidade
            multiplicacao = {
                'jan': 2 * float(data.t_med_jan),
                'fev': 2 * float(data.t_med_fev),
                'mar': 2 * float(data.t_med_mar),
                'abr': 2 * float(data.t_med_abr),
                'mai': 2 * float(data.t_med_mai),
                'jun': 2 * float(data.t_med_jun),
                'jul': 2 * float(data.t_med_jul),
                'ago': 2 * float(data.t_med_ago),
                'set': 2 * float(data.t_med_set),
                'out': 2 * float(data.t_med_out),
                'nov': 2 * float(data.t_med_nov),
                'dez': 2 * float(data.t_med_dez),
            }
        else:
            multiplicacao = {}

        return render(request, 'index.html', {
            'city_list': city_list,
            'uf_list': uf_list,
            'data': data,
            'multiplicacao': multiplicacao,
            'cidade_selecionada': cidade_selecionada# Passa o dicionário com a multiplicação de cada mês
        })
    
    return render(request, 'index.html', {'city_list': city_list, 'uf_list': uf_list})
    
def table(request): 
    city = request.GET.get('cidade')
    #list = Precipitacao.objects.all().filter(cidade=city)
    #return render(request, 'tabela.html', {'list':list})
    return render(request, 'tabela.html')

def login(request):
    return render(request, 'login.html')


def devs(request):
    return render(request, 'devs.html')
# Create your views here.
