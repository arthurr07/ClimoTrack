from django.contrib import admin
from app.models import DadosHidricos, Cidade

class DadosHidricosList(admin.ModelAdmin):
    list_display = ('cidade', 'bal_hidrico', 'ind_pluviometricos', 'precipitacao')
    list_display_links = ('cidade', 'bal_hidrico', 'ind_pluviometricos', 'precipitacao')
    search_fields = ('cidade', 'bal_hidrico')

class CidadeList(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome')




admin.site.register(DadosHidricos, DadosHidricosList)
admin.site.register(Cidade, CidadeList)
# Register your models here.
