from django.contrib import admin
from app.models import DadosHidricos, Cidade, Estado, Precipitacao


class EstadoFilter(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome')
    
class CidadeFilter(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome')
    
class PrecipitacaoFilter(admin.ModelAdmin):
    list_display = ('id', 'cidade', 'data_hora', 'precipitacao')
    list_display_links = ('id', 'cidade', 'data_hora', 'precipitacao') 
    search_fields = ('id', 'cidade', 'data_hora', 'precipitacao')

admin.site.register(Estado, EstadoFilter)
admin.site.register(Cidade, CidadeFilter)
admin.site.register(Precipitacao, PrecipitacaoFilter)

# Register your models here.

