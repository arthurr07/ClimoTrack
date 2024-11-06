from django.db import models

# Create your models here.
class DadosHidricos(models.Model):
    cidade = models.CharField(null = False, max_length = 100)
    ind_pluviometricos = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    bal_hidrico = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    precipitacao = models.DecimalField(null = False, max_digits = 10, decimal_places = 4)
    
    
class Cidade(models.Model):
    nome = models.CharField(null = False, max_length = 100)
    