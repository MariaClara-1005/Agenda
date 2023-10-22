from django.db import models
from typing import Text

class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    funcao = models.CharField(max_length=30)
    descricao = models.CharField(max_length=500)
