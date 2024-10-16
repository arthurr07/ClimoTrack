from django.contrib import admin
from app.models import DadosHidricos

class DadosHidricosList(admin.ModelAdmin):
    list_display = ('cidade', 'bal_hidrico', 'ind_pluviometricos', 'precipitacao')
    list_display_links = ('cidade', 'bal_hidrico', 'ind_pluviometricos', 'precipitacao')
    search_fields = ('cidade', 'bal_hidrico')





admin.site.register(DadosHidricos, DadosHidricosList)
# Register your models here.
