# models.py
from django.db import models

class Profissao(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    profissao = models.ForeignKey(Profissao, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome
