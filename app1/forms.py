from django import forms
from .models import Pessoa, Profissao

class ProfissaoForm(forms.ModelForm):
    class Meta:
        model = Profissao
        fields = ['descricao']
        labels = {
            'descricao': 'Cadastrar Profissão',
        }


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'cpf', 'data_nascimento', 'profissao']
        error_messages = {
            'profissao': {
                'invalid_choice': 'erro',
            },
        }
