from django.db import models
    
class Estado(models.Model):
    nome = models.CharField(null = False, max_length = 100)
    
    def __str__(self) -> str:
        return self.nome
    
class Cidade(models.Model):
    estacao = models.CharField(null = False, max_length = 100)
    estado = models.ForeignKey(Estado, on_delete = models.CASCADE, default=1)
    
    def __str__(self) -> str:
        return self.estacao
    
class DadosHidricos(models.Model):
    estacao = models.ForeignKey(Cidade, on_delete = models.CASCADE, default=1)
    t_med_jan = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    t_med_fev = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    t_med_mar = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    t_med_abr = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    t_med_mai = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    t_med_jun = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    t_med_jul = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    t_med_ago = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    t_med_set = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    t_med_out = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    t_med_nov = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    t_med_dez = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    precip_md_jan = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    precip_md_fev = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    precip_md_mar = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    precip_md_abr = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    precip_md_mai = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    precip_md_jun = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    precip_md_jul = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    precip_md_ago = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    precip_md_set = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    precip_md_out = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    precip_md_nov = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    precip_md_dez = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    
