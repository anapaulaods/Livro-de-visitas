from django.db import models

# Create your models here.
class Recado(models.Model):
    nome = models.CharField(max_length=200)
    mensagem = models.CharField(max_length=200)

