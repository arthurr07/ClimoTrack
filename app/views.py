from django.shortcuts import render
from app.models import DadosHidricos
def index(request):
    return render(request, 'index.html')

def table(request): 
    list = DadosHidricos.objects.all()
    return render(request, 'tabela.html', {'list':list})
# Create your views here.
