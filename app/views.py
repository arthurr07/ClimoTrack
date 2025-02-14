from django.shortcuts import render
from app.models import Cidade, DadosHidricos, Estado
def index(request):
    city_list = Cidade.objects.all()
    uf_list = Estado.objects.all()

    if request.method == "POST":
        cidade = int(request.POST['cidade'])
        data = DadosHidricos.objects.filter(estacao=cidade).first()
        cidade_selecionada = Cidade.objects.get(id=cidade)
        total = 0
        
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
                'med_temp': round((data.t_med_jan + data.t_med_fev + data.t_med_mar + data.t_med_abr + data.t_med_mai + data.t_med_jun + data.t_med_jul + data.t_med_ago + data.t_med_set + data.t_med_out 
                             + data.t_med_nov + data.t_med_dez)/12,4),
                'med_precip': round((data.precip_md_jan + data.precip_md_fev + data.precip_md_mar + data.precip_md_abr + data.precip_md_mai + data.precip_md_jun + data.precip_md_jul + data.precip_md_ago + data.precip_md_set + data.precip_md_out 
                             + data.precip_md_nov + data.precip_md_dez)/12,4),
            }
            if  data.precip_md_jan <= multiplicacao.get('jan') : total = total+1
            if  data.precip_md_fev <= multiplicacao.get('fev') : total = total+1
            if  data.precip_md_mar <= multiplicacao.get('mar') : total = total+1
            if  data.precip_md_abr <= multiplicacao.get('abr') : total = total+1
            if  data.precip_md_mai <= multiplicacao.get('mai') : total = total+1
            if  data.precip_md_jun <= multiplicacao.get('jun') : total = total+1
            if  data.precip_md_jul <= multiplicacao.get('jul') : total = total+1
            if  data.precip_md_ago <= multiplicacao.get('ago') : total = total+1
            if  data.precip_md_set <= multiplicacao.get('set') : total = total+1
            if  data.precip_md_out <= multiplicacao.get('out') : total = total+1
            if  data.precip_md_nov <= multiplicacao.get('nov') : total = total+1
            if  data.precip_md_dez <= multiplicacao.get('dez') : total = total+1
            
        else:
            multiplicacao = {}
        
            

        return render(request, 'index.html', {
            'city_list': city_list,
            'uf_list': uf_list,
            'data': data,
            'multiplicacao': multiplicacao,
            'cidade_selecionada': cidade_selecionada,
            'total':total
            # Passa o dicionário com a multiplicação de cada mês
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
