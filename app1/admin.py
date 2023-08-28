from django.contrib import admin
from .models import Profissao, Pessoa

class ProfissaoAdmin(admin.ModelAdmin):
    list_display = ('profissão')

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'data_nascimento', 'profissao')


admin.site.register(Profissao)
admin.site.register(Pessoa)
